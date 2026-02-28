import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';
import 'dart:async';
import 'dart:io';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return const MaterialApp(
      debugShowCheckedModeBanner: false,
      home: SniperDashboardScreen(),
    );
  }
}

//////////////////////////////////////////////////////////////
// 🏠 ADD SNIPE SCREEN & SNIPER DASHBOARD COMBINED
//////////////////////////////////////////////////////////////

class SniperDashboardScreen extends StatefulWidget {
  const SniperDashboardScreen({super.key});

  @override
  State<SniperDashboardScreen> createState() => _SniperDashboardScreenState();
}

class _SniperDashboardScreenState extends State<SniperDashboardScreen> {
  // Variables for the form (Add Snipe)
  final TextEditingController urlController = TextEditingController();
  final TextEditingController priceController = TextEditingController();
  bool isLoading = false;

  // Variables for the Snipes List (Dashboard)
  List<dynamic> snipes = [];
  Timer? _timer;

  // Configuration
  // 🔴 IMPORTANT: Replace with your actual Railway backend URL
  // Configuration
  // Use build-time define to set the backend URL. Example:
  // flutter build apk --release --dart-define=BACKEND_URL="https://your-railway-app.up.railway.app"
  static const String backendUrl = String.fromEnvironment(
    'BACKEND_URL',
    defaultValue: 'https://your-railway-app-name.up.railway.app',
  );
  late final String apiUrl = "$backendUrl/get_snipes";
  late final String addApi = "$backendUrl/add_snipe";
  static const Duration requestTimeout = Duration(seconds: 10);

  // Logging helper
  void _log(String message) {
    final timestamp = DateTime.now().toIso8601String();
    print('[SNIPER_APP] [$timestamp] $message');
  }

  // Add new Snipe to the Backend
  Future<void> addSnipe() async {
    // Validate inputs
    final urlText = urlController.text.trim();
    final priceText = priceController.text.trim();

    if (urlText.isEmpty || priceText.isEmpty) {
      _log("Validation failed: empty inputs");
      ScaffoldMessenger.of(context).showSnackBar(
        const SnackBar(content: Text("Please fill in all fields")),
      );
      return;
    }

    // Validate URL format
    final uri = Uri.tryParse(urlText);
    if (uri == null || !uri.hasScheme) {
      _log("Validation failed: invalid URL format - $urlText");
      ScaffoldMessenger.of(context).showSnackBar(
        const SnackBar(
          content: Text("Please enter a valid URL (e.g., https://example.com)"),
        ),
      );
      return;
    }

    // Validate and parse price
    double targetPrice;
    try {
      targetPrice = double.parse(priceText);
    } on FormatException {
      _log("Validation failed: invalid price format - $priceText");
      ScaffoldMessenger.of(context).showSnackBar(
        const SnackBar(content: Text("Please enter a valid number for price")),
      );
      return;
    }

    // Validate price value
    if (targetPrice <= 0) {
      _log("Validation failed: price must be positive - $targetPrice");
      ScaffoldMessenger.of(context).showSnackBar(
        const SnackBar(content: Text("Price must be greater than 0")),
      );
      return;
    }

    setState(() => isLoading = true);
    _log("Adding snipe: url=$urlText, target_price=$targetPrice");

    try {
      _log("Sending POST request to $addApi");
      final response = await http
          .post(
            Uri.parse(addApi),
            headers: {"Content-Type": "application/json"},
            body: jsonEncode({"url": urlText, "target_price": targetPrice}),
          )
          .timeout(requestTimeout);

      _log(
        "Response received: status=${response.statusCode}, body=${response.body}",
      );

      setState(() => isLoading = false);

      if (response.statusCode == 200) {
        _log("Snipe added successfully!");
        fetchSnipes(); // Fetch the updated snipes list
        urlController.clear(); // Clear input fields
        priceController.clear();
        ScaffoldMessenger.of(context).showSnackBar(
          const SnackBar(content: Text("Snipe added successfully!")),
        );
        Navigator.pop(context); // Close the bottom sheet
      } else if (response.statusCode == 400) {
        _log("Client error: ${response.body}");
        ScaffoldMessenger.of(context).showSnackBar(
          SnackBar(content: Text("Invalid input: ${response.body}")),
        );
      } else if (response.statusCode == 500) {
        _log("Server error: ${response.body}");
        ScaffoldMessenger.of(context).showSnackBar(
          const SnackBar(
            content: Text("Backend server error. Please try again."),
          ),
        );
      } else {
        _log("Unexpected status code: ${response.statusCode}");
        ScaffoldMessenger.of(context).showSnackBar(
          SnackBar(
            content: Text("Error: ${response.statusCode} - ${response.body}"),
          ),
        );
      }
    } on TimeoutException {
      _log("Error: Request timed out (10 second timeout)");
      setState(() => isLoading = false);
      ScaffoldMessenger.of(context).showSnackBar(
        const SnackBar(
          content: Text("Request timed out. Backend may be unreachable."),
        ),
      );
    } on SocketException catch (e) {
      _log("Error: Network error - $e");
      setState(() => isLoading = false);
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(
          content: Text("Network error: Cannot reach backend at $backendUrl"),
        ),
      );
    } catch (e) {
      _log("Error: Unexpected exception - $e");
      setState(() => isLoading = false);
      ScaffoldMessenger.of(
        context,
      ).showSnackBar(SnackBar(content: Text("Error: ${e.toString()}")));
    }
  }

  // Fetch snipes from backend
  Future<void> fetchSnipes() async {
    _log("Fetching snipes from $apiUrl");
    try {
      final response = await http
          .get(Uri.parse(apiUrl))
          .timeout(requestTimeout);
      _log(
        "Snipes response: status=${response.statusCode}, body=${response.body}",
      );

      if (response.statusCode == 200) {
        try {
          final data = jsonDecode(response.body);

          // Validate response structure
          if (!data.containsKey("snipes")) {
            _log("Warning: Response missing 'snipes' key");
            return;
          }

          if (data["snipes"] is! List) {
            _log(
              "Warning: 'snipes' is not a list: ${data["snipes"].runtimeType}",
            );
            return;
          }

          setState(() {
            snipes = data["snipes"] as List<dynamic>;
          });
          _log("Snipes updated: ${snipes.length} items");
        } on FormatException catch (e) {
          _log("Error: Failed to parse JSON response - $e");
        }
      } else if (response.statusCode == 404) {
        _log("Error: Endpoint not found (404) - Check backend URL");
      } else if (response.statusCode == 500) {
        _log("Error: Backend server error (500)");
      } else {
        _log("Error: Unexpected status code ${response.statusCode}");
      }
    } on TimeoutException {
      _log(
        "Error: Fetch request timed out (10 second timeout) - Backend may be unresponsive",
      );
    } on SocketException catch (e) {
      _log(
        "Error: Network error while fetching snipes - $e. Cannot reach $backendUrl",
      );
    } catch (e) {
      _log("Error: Unexpected exception while fetching - $e");
    }
  }

  // Auto fetch snipes every 5 seconds
  @override
  void initState() {
    super.initState();
    fetchSnipes();
    _timer = Timer.periodic(const Duration(seconds: 5), (_) => fetchSnipes());
  }

  @override
  void dispose() {
    _timer?.cancel();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("Sniper Dashboard"),
        actions: [
          IconButton(
            icon: const Icon(Icons.add),
            onPressed: () {
              showModalBottomSheet(
                context: context,
                builder: (BuildContext context) {
                  return Padding(
                    padding: const EdgeInsets.all(20),
                    child: Column(
                      mainAxisSize: MainAxisSize.min,
                      children: [
                        const Text(
                          "Activate New Sniper",
                          style: TextStyle(
                            fontSize: 22,
                            fontWeight: FontWeight.bold,
                          ),
                        ),
                        const SizedBox(height: 30),
                        TextField(
                          controller: urlController,
                          decoration: InputDecoration(
                            labelText: "Product URL",
                            border: OutlineInputBorder(
                              borderRadius: BorderRadius.circular(12),
                            ),
                          ),
                        ),
                        const SizedBox(height: 20),
                        TextField(
                          controller: priceController,
                          keyboardType: TextInputType.number,
                          decoration: InputDecoration(
                            labelText: "Target Price",
                            border: OutlineInputBorder(
                              borderRadius: BorderRadius.circular(12),
                            ),
                          ),
                        ),
                        const SizedBox(height: 30),
                        SizedBox(
                          width: double.infinity,
                          child: ElevatedButton(
                            onPressed: isLoading ? null : addSnipe,
                            style: ElevatedButton.styleFrom(
                              padding: const EdgeInsets.all(16),
                              shape: RoundedRectangleBorder(
                                borderRadius: BorderRadius.circular(12),
                              ),
                            ),
                            child: isLoading
                                ? const CircularProgressIndicator(
                                    color: Colors.white,
                                  )
                                : const Text(
                                    "Activate Sniper",
                                    style: TextStyle(fontSize: 16),
                                  ),
                          ),
                        ),
                      ],
                    ),
                  );
                },
              );
            },
          ),
        ],
      ),
      body: snipes.isEmpty
          ? const Center(child: Text("No snipes yet"))
          : ListView.builder(
              itemCount: snipes.length,
              itemBuilder: (context, index) {
                final snipe = snipes[index];

                return Card(
                  margin: const EdgeInsets.all(12),
                  child: ListTile(
                    title: Text("Target: ${snipe['target_price']}"),
                    subtitle: Text("Current: ${snipe['current_price']}"),
                    trailing: Text(
                      snipe['status'],
                      style: TextStyle(
                        color: snipe['status'] == "Target Hit"
                            ? Colors.green
                            : Colors.orange,
                        fontWeight: FontWeight.bold,
                      ),
                    ),
                  ),
                );
              },
            ),
    );
  }
}
