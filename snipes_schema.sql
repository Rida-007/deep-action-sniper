-- Create snipes table for Deep Action Sniper
CREATE TABLE IF NOT EXISTS snipes (
  id INT AUTO_INCREMENT PRIMARY KEY,
  url TEXT NULL,
  target_price FLOAT NULL,
  current_price FLOAT NULL,
  status VARCHAR(50) NULL,
  created_at TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP
);
