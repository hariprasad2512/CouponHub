CREATE DATABASE IF NOT EXISTS couponhub;
USE couponhub;

CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);

CREATE TABLE coupons (
    coupon_id INT AUTO_INCREMENT PRIMARY KEY,
    coupon_name VARCHAR(100) NOT NULL,
    code VARCHAR(50) UNIQUE NOT NULL,
    discount_pct INT NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    expiry_date DATETIME NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    purchased_by_user_id INT NULL,
    FOREIGN KEY (purchased_by_user_id) REFERENCES users(user_id)
);


CREATE TABLE transactions (
    transaction_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    coupon_id INT,
    amount_paid DECIMAL(10, 2) NOT NULL,
    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status ENUM('SUCCESS', 'FAILED') DEFAULT 'SUCCESS',
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (coupon_id) REFERENCES coupons(coupon_id) ON DELETE CASCADE
);

CREATE TABLE redemptions (
    redemption_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    coupon_id INT,
    redeemed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (coupon_id) REFERENCES coupons(coupon_id) ON DELETE CASCADE
);
