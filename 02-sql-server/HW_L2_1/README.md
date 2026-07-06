# Data Science Bootcamp - SQL & Database Analysis Homework (HW_L2_4)

این مخزن شامل پاسخ تکالیف و کوئری‌های تحلیل دیتابیس در پلتفرم SQL Server برای بخش تراکنش‌های مالی و مدیریت اطلاعات پایانه‌ها در بوت‌کمپ دیتاساینس است.
This repository contains SQL queries for database analysis, focuses on banking transactions, terminal performance tracking, and merchant workflow analysis.

---

## 📌 شرح کوئری‌ها و تحلیل‌ها (SQL Queries Description)

### 1️⃣ فیلتر تراکنش‌های بزرگ بازه زمانی خاص (High-Value Transactions Filter)
* **توضیحات (FA):** استخراج تمامی تراکنش‌های بدون مقدار تهی با مبلغ بیش از ۱۰۰,۰۰۰ تومان در بازه زمانی ۲۵ دی تا ۲۴ بهمن ۱۴۰۱ به صورت مرتب شده[cite: 19].
* **Description (EN):** Selects all non-null transactions with an amount exceeding 100K between 25 Dey and 24 Bahman 1401, sorted chronologically[cite: 19].

### 2️⃣ وضعیت مدارک پذیرندگان (Merchants Documentation Workflow)
* **توضیحات (FA):** استخراج نام فروشگاه، نام استان، شهر و شماره ترمینال مربوط به پذیرندگانی که در وضعیت گردش‌کار "تکمیل مدارک" قرار دارند[cite: 20].
* **Description (EN):** Extracts shop names, provinces, cities, and terminal numbers for merchants with a "تکمیل مدارک" (Documents Completed) workflow status[cite: 20].

### 3️⃣ تحلیل رفتار پایانه‌های فعال دی ماه در بهمن (Dey Active Terminals Performance in Bahman)
* **توضیحات (FA):** استخراج تراکنش‌های بهمن ماه برای پایانه‌هایی که در دی ماه مجموعاً تراکنشی با ارزش بیش از ۲۰۰,۰۰۰ تومان ثبت کرده‌اند[cite: 21].
* **Description (EN):** Retrieves Bahman transactions for specific terminals that registered transactions greater than 200K during Dey[cite: 21].

### 4️⃣ برترین تراکنش‌های استان آذربایجان شرقی (Top 5 Transactions in East Azerbaijan)
* **توضیحات (FA):** نمایش ۵ تراکنش برتر غیرصفر اسفند ماه مربوط به پایانه‌های مستقر در استان آذربایجان شرقی به صورت صعودی[cite: 22].
* **Description (EN):** Fetches the top 5 non-zero Esfand transactions for terminals located in the "آذربايجان شرقي" province, sorted by amount[cite: 22].

### 5️⃣ مجموع عملکرد پایانه‌ها در بهمن ماه (Terminal Monthly Aggregation)
* **توضیحات (FA):** محاسبه مجموع کل مبالغ و تعداد تراکنش‌های بهمن ماه به تفکیک هر پایانه، به صورت نزولی بر اساس بالاترین مبالغ تراکنش[cite: 23].
* **Description (EN):** Calculates the total transaction amount and count per terminal in Bahman, ordered by total volume descending[cite: 23].

### 6️⃣ عملکرد روزانه پایانه‌ها (Daily Terminal Performance Metrics)
* **توضیحات (FA):** محاسبه بالاترین مبلغ تراکنش روزانه و تعداد تراکنش‌های هر ترمینال به تفکیک تاریخ[cite: 24].
* **Description (EN):** Evaluates daily maximum transaction amounts and total transaction counts grouped by date and terminal number[cite: 24].

### 7️⃣ عملکرد پایانه‌های غیرفعال در اسفند ماه (Inactive Terminals Recovery Analysis)
* **توضیحات (FA):** محاسبه مجموع درآمد اسفند ماه پایانه‌هایی که در بهمن ماه کاملاً غیرفعال بوده یا مبلغ تراکنش آن‌ها صفر بوده است[cite: 25].
* **Description (EN):** Analyzes Esfand transaction totals for terminals that were completely inactive (amount = 0) during Bahman[cite: 25].

---

## 👨‍💻 نویسنده (Author)
* **Zargol Kanani** (زرگل کنعانی)
