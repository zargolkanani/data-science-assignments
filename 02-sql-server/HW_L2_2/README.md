# Data Science Bootcamp - Advanced SQL & Banking Transaction Analysis (HW_L2_2)

این مخزن شامل سری دوم تکالیف و کوئری‌های پیشرفته پایگاه داده (SQL Server) جهت تحلیل رفتار تراکنش‌های بانکی، محاسبه کارمزد پایانه بر اساس نوع تراکنش و ارزیابی عملکرد فروشگاه‌ها در بوت‌کمپ دیتاساینس است.
This repository contains advanced SQL queries analyzing banking transactions, dynamic fee structures, terminal performance indicators, and regional metrics.

---

## 📂 ساختار فایل‌های پروژه (File Structure)

* `SQLQuery1.sql`: کوئری فیلتر شهرهای پرتراکنش‌تر از میانگین کل.
* `SQLQuery2.sql`: کوئری استخراج فروشگاه‌ها و پایانه‌های غیرفعال یا با تراکنش صفر.
* `SQLQuery3.sql`: کوئری مقایسه مجموع تراکنش‌های استان‌های البرز و خوزستان در بهمن ۱۴۰۱.
* `SQLQuery4.sql`: کوئری محاسبه ماهانه کارمزد پایانه‌ها بر اساس نوع و مبلغ تراکنش (خرید، مانده‌گیری، شارژ).
* `SQLQuery5.sql`: کوئری تحلیل آماری تفکیکی انواع تراکنش‌ها و مبالغ در دی ماه ۱۴۰۱.

---

## 📌 شرح کوئری‌ها و منطق تحلیل (SQL Queries Analysis)

### 1️⃣ شهرهای گران‌تر از میانگین (High-Volume Transaction Cities)
* **توضیحات (FA):** اتصال جدول تراکنش‌ها و پذیرندگان جهت محاسبه میانگین مبالغ و تعداد تراکنش‌ها به تفکیک شهر و فیلتر کردن شهرهایی که میانگین آن‌ها از میانگین کل تراکنش‌های دیتابیس بالاتر است (با استفاده از `HAVING` و `Subquery`).
* **Description (EN):** Joins transactions and merchants tables to find cities where the average transaction amount exceeds the overall platform average, using conditional grouping (`HAVING`).

### 2️⃣ فروشگاه‌های در عمل غیرفعال (Inactive Merchants Recovery)
* **توضیحات (FA):** استفاده از `LEFT JOIN` برای استخراج شماره پایانه و نام فروشگاه‌هایی که هیچ تراکنشی برای آن‌ها ثبت نشده یا مجموع مبالغ تراکنش آن‌ها صفر بوده است.
* **Description (EN):** Employs a `LEFT JOIN` to safely identify terminals and shop names that either recorded zero transactions or a cumulative volume of zero.

### 3️⃣ مقایسه عملکرد استان‌های البرز و خوزستان (Regional Performance Benchmarking)
* **توضیحات (FA):** محاسبه و مقایسه مجموع کل تراکنش‌های ثبت شده برای پایانه‌های استان البرز و خوزستان به طور خاص در بازه زمانی بهمن ماه ۱۴۰۱.
* **Description (EN):** Aggregates and compares the total transaction amounts between Alborz and Khuzestan provinces specifically within the Bahman 1401 Persian date range.

### 4️⃣ محاسبه کارمزد پایانی ماهانه (Dynamic Terminal Fee Calculation)
* **توضیحات (FA):** پیاده‌سازی منطق فرمول کارمزد با دستور `CASE WHEN` به تفکیک نوع تراکنش (مانده‌گیری: ۲۰۰، شارژ: ۱۰۰، خرید زیر ۵ هزار تومان: ۲۵، خرید بین ۵ تا ۲۵ هزار تومان: ٪۱ و بالای ۲۵ هزار تومان: ۲۶۰ تومان) برای هر پایانه در هر ماه.
* **Description (EN):** Implements complex conditional logic (`CASE WHEN`) to dynamically calculate custom monthly terminal fee structures split by transaction types (purchases, balance inquiries, mobile top-ups).

### 5️⃣ آمار تفکیکی عملکرد پایانه‌ها در دی ماه (Detailed Dey 1401 Metrics)
* **توضیحات (FA):** استخراج آمار جامع شامل تعداد کل تراکنش‌ها، تعداد تفکیک‌شده تراکنش‌های خرید، مانده‌گیری و شارژ به همراه مجموع درآمد هر پایانه در دی ماه ۱۴۰۱ به صورت نزولی.
* **Description (EN):** Generates comprehensive monthly statistics tracking total counts, specific transaction categories (Buy, Balance, Charge), and total volumes per terminal for Dey 1401.

---

## 👨‍💻 نویسنده (Author)
* **Zargol Kanani** (زرگل کنعانی)
