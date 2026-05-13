import streamlit as st
import smtplib
import requests
import urllib.parse
from email.mime.text import MIMEText

# -----------------------------------------------------
# १. Mitradnya Publication - Email Setup
# -----------------------------------------------------
TEACHER_EMAIL = "vidyarthi.mitradnyapublications@gmail.com" 
EMAIL_PASSWORD = "vhoc lltr ejwu qomk"   
TEACHER_NAME = "Mukesh Sir"

def send_score_to_teacher(student_name, div, roll, score, total, chapter, test_name):
    msg_content = f"📚 Online Exam's Result Alert 📚!\n\nStudent Name: {student_name}\nDivision: {div}\nRoll No: {roll}\nChapter: {chapter}\nTest: {test_name}\nScore: {score}/{total}"
    msg = MIMEText(msg_content)
    msg['Subject'] = f"New Quiz Result: {student_name} ({div}-{roll}) scored {score}/{total} in {chapter}"
    msg['From'] = TEACHER_NAME
    msg['To'] = TEACHER_NAME

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(TEACHER_EMAIL, EMAIL_PASSWORD)
        server.sendmail(TEACHER_EMAIL, TEACHER_EMAIL, msg.as_string())
        server.quit()
        return True
    except Exception as e:
        return False

# -----------------------------------------------------
# २. सर्व प्रश्नांचा डेटाबेस (Chapter 1, 2, 3)
# -----------------------------------------------------

# --- CHAPTER 1: PARTNERSHIP FINAL ACCOUNTS (100 Qs) ---
quiz_data_partnership = [
    {"q": "1. The Indian Partnership Act was passed in the year:", "options": ["1923", "1932", "1956", "2013"], "ans": "1932"},
    {"q": "2. The liability of partners in a standard partnership firm is:", "options": ["Limited", "Unlimited", "Zero", "Joint only"], "ans": "Unlimited"},
    {"q": "3. The document containing the terms of the partnership agreement is called:", "options": ["Partnership Deed", "Prospectus", "Articles", "Memorandum"], "ans": "Partnership Deed"},
    {"q": "4. In the absence of a Partnership Deed, profits and losses are shared:", "options": ["In Capital Ratio", "In Time Ratio", "Equally", "As per work"], "ans": "Equally"},
    {"q": "5. Registration of a Partnership Firm is compulsory in the state of:", "options": ["Gujarat", "Maharashtra", "Delhi", "Goa"], "ans": "Maharashtra"},
    {"q": "6. In the absence of an agreement, interest on partner's loan is allowed at:", "options": ["5% p.a.", "6% p.a.", "8% p.a.", "10% p.a."], "ans": "6% p.a."},
    {"q": "7. Closing stock is always valued at Cost Price or Market Price, whichever is:", "options": ["Higher", "Lower", "Equal", "None"], "ans": "Lower"},
    {"q": "8. Wages and Salaries appearing in the Trial Balance are shown in:", "options": ["Trading A/c", "Profit & Loss A/c", "Balance Sheet", "Capital A/c"], "ans": "Trading A/c"},
    {"q": "9. Salaries and Wages appearing in the Trial Balance are shown in:", "options": ["Trading A/c", "Profit & Loss A/c", "Balance Sheet", "Capital A/c"], "ans": "Profit & Loss A/c"},
    {"q": "10. Carriage Inward is debited to:", "options": ["Trading A/c", "Profit & Loss A/c", "Partners' Capital A/c", "Balance Sheet"], "ans": "Trading A/c"},
    {"q": "11. Carriage Outward is debited to:", "options": ["Trading A/c", "Profit & Loss A/c", "Partners' Capital A/c", "Balance Sheet"], "ans": "Profit & Loss A/c"},
    {"q": "12. Return Outward is deducted from:", "options": ["Sales", "Purchases", "Capital", "Debtors"], "ans": "Purchases"},
    {"q": "13. Return Inward is deducted from:", "options": ["Sales", "Purchases", "Capital", "Debtors"], "ans": "Sales"},
    {"q": "14. Prepaid expenses are shown on the:", "options": ["Asset side", "Liability side", "Debit of P&L", "Credit of Trading"], "ans": "Asset side"},
    {"q": "15. Outstanding expenses are shown on the:", "options": ["Asset side", "Liability side", "Debit of Trading", "Credit of P&L"], "ans": "Liability side"},
    {"q": "16. Bad debts are written off against:", "options": ["Creditors", "Bills Receivable", "Debtors", "Cash"], "ans": "Debtors"},
    {"q": "17. Provision for doubtful debts (RDD) is calculated on:", "options": ["Creditors", "Net Sales", "Debtors", "Bills Payable"], "ans": "Debtors"},
    {"q": "18. Depreciation is a charge against:", "options": ["Assets", "Liabilities", "Capital", "Cash"], "ans": "Assets"},
    {"q": "19. Depreciation is shown on the debit side of:", "options": ["Trading A/c", "Profit & Loss A/c", "Balance Sheet", "Partners A/c"], "ans": "Profit & Loss A/c"},
    {"q": "20. Goods distributed as free samples are credited to:", "options": ["Trading A/c", "Profit & Loss A/c", "Capital A/c", "Balance Sheet"], "ans": "Trading A/c"},
    {"q": "21. Goods distributed as free samples are debited to P&L A/c as:", "options": ["Purchases", "Advertisement", "Charity", "Discount"], "ans": "Advertisement"},
    {"q": "22. Goods withdrawn by a partner for personal use is called:", "options": ["Capital", "Drawings", "Investment", "Salary"], "ans": "Drawings"},
    {"q": "23. Interest on drawings is a/an ________ for the partnership firm.", "options": ["Expense", "Income", "Asset", "Liability"], "ans": "Income"},
    {"q": "24. Interest on capital is a/an ________ for the partnership firm.", "options": ["Expense", "Income", "Asset", "Liability"], "ans": "Expense"},
    {"q": "25. If there are Fixed Capital Accounts, all adjustments are made in:", "options": ["Capital A/c", "Current A/c", "Suspense A/c", "Loan A/c"], "ans": "Current A/c"},
    {"q": "26. If the Capital method is Fluctuating, all adjustments are made in:", "options": ["Capital A/c", "Current A/c", "Suspense A/c", "Cash A/c"], "ans": "Capital A/c"},
    {"q": "27. Gross Profit is transferred to the ________ side of the Profit & Loss A/c.", "options": ["Debit", "Credit", "Asset", "Liability"], "ans": "Credit"},
    {"q": "28. Net Profit is transferred to the ________ of Partners' Capital/Current A/c.", "options": ["Debit", "Credit", "Asset", "Liability"], "ans": "Credit"},
    {"q": "29. The debit balance of the Trading Account indicates:", "options": ["Gross Profit", "Gross Loss", "Net Profit", "Net Loss"], "ans": "Gross Loss"},
    {"q": "30. The credit balance of the Profit & Loss Account indicates:", "options": ["Gross Profit", "Gross Loss", "Net Profit", "Net Loss"], "ans": "Net Profit"},
    {"q": "31. Bills Receivable discounted but dishonoured is added to:", "options": ["Debtors", "Creditors", "Cash", "Capital"], "ans": "Debtors"},
    {"q": "32. Interest on Partner's Loan is debited to:", "options": ["Trading A/c", "Profit & Loss A/c", "Capital A/c", "Asset"], "ans": "Profit & Loss A/c"},
    {"q": "33. Unrecorded purchases are added to Purchases and:", "options": ["Debtors", "Creditors", "Bills Payable", "Capital"], "ans": "Creditors"},
    {"q": "34. Unrecorded sales are added to Sales and:", "options": ["Debtors", "Creditors", "Cash", "Stock"], "ans": "Debtors"},
    {"q": "35. Goods destroyed by fire (fully insured), the insurance claim is an:", "options": ["Expense", "Asset", "Liability", "Income"], "ans": "Asset"},
    {"q": "36. Royalty paid on production is debited to:", "options": ["Trading A/c", "Profit & Loss A/c", "Balance Sheet", "Capital A/c"], "ans": "Trading A/c"},
    {"q": "37. Royalty paid on sales is debited to:", "options": ["Trading A/c", "Profit & Loss A/c", "Balance Sheet", "Capital A/c"], "ans": "Profit & Loss A/c"},
    {"q": "38. Commission received in advance is a/an:", "options": ["Asset", "Liability", "Income", "Expense"], "ans": "Liability"},
    {"q": "39. Income accrued but not received is shown on the:", "options": ["Asset side", "Liability side", "Debit of P&L", "Credit of Trading"], "ans": "Asset side"},
    {"q": "40. Bank Overdraft is shown under:", "options": ["Fixed Assets", "Current Liabilities", "Current Assets", "Investments"], "ans": "Current Liabilities"},
    {"q": "41. Goodwill is an example of a/an:", "options": ["Tangible Asset", "Intangible Asset", "Fictitious Asset", "Current Asset"], "ans": "Intangible Asset"},
    {"q": "42. Patents and Trademarks appear on which side of the Balance Sheet?", "options": ["Asset", "Liability", "Both", "None"], "ans": "Asset"},
    {"q": "43. Provident Fund contribution by the employer is debited to:", "options": ["Trading A/c", "Profit & Loss A/c", "Capital A/c", "Balance Sheet"], "ans": "Profit & Loss A/c"},
    {"q": "44. Cash in hand is a/an:", "options": ["Current Asset", "Fixed Asset", "Intangible Asset", "Liability"], "ans": "Current Asset"},
    {"q": "45. Discount allowed is shown on the debit side of:", "options": ["Trading A/c", "Profit & Loss A/c", "Capital A/c", "Balance Sheet"], "ans": "Profit & Loss A/c"},
    {"q": "46. Partners share profit/loss in their _________ ratio.", "options": ["Capital", "Sacrifice", "Profit Sharing", "Gain"], "ans": "Profit Sharing"},
    {"q": "47. Balance Sheet is a statement showing:", "options": ["Income & Expenses", "Financial Position", "Cash flow", "Production"], "ans": "Financial Position"},
    {"q": "48. Factory lighting is debited to:", "options": ["Trading A/c", "Profit & Loss A/c", "Capital A/c", "Balance Sheet"], "ans": "Trading A/c"},
    {"q": "49. Office lighting is debited to:", "options": ["Trading A/c", "Profit & Loss A/c", "Capital A/c", "Balance Sheet"], "ans": "Profit & Loss A/c"},
    {"q": "50. An amount which cannot be recovered from Debtors is called:", "options": ["Discount", "Bad Debts", "Drawings", "Charity"], "ans": "Bad Debts"},
    {"q": "51. If 'Rent (for 10 months) ₹10,000' is given in the Trial Balance, what is the Outstanding Rent amount?", "options": ["₹2,000", "₹1,000", "₹5,000", "No Outstanding"], "ans": "₹2,000"},
    {"q": "52. If 'Insurance (for 15 months) ₹15,000' is given, what is the Prepaid Insurance?", "options": ["₹3,000", "₹5,000", "₹12,000", "₹1,000"], "ans": "₹3,000"},
    {"q": "53. Advertisement for 3 years ₹30,000. Amount for current year is:", "options": ["₹10,000", "₹30,000", "₹20,000", "₹15,000"], "ans": "₹10,000"},
    {"q": "54. 10% Bank Loan ₹50,000 taken on 1st Oct. Interest for 6 months is:", "options": ["₹2,500", "₹5,000", "₹1,250", "₹500"], "ans": "₹2,500"},
    {"q": "55. Accrued Interest on Govt Bonds is shown on:", "options": ["Asset side", "Liability side", "Trading Dr", "P&L Cr"], "ans": "Asset side"},
    {"q": "56. Goods worth ₹5,000 destroyed by fire, insurance claim ₹3,000. Net loss to P&L is:", "options": ["₹2,000", "₹5,000", "₹3,000", "₹8,000"], "ans": "₹2,000"},
    {"q": "57. Uninsured goods stolen. Effects are:", "options": ["Trading Cr & P&L Dr", "Trading Cr & Asset", "Trading Cr & Liability", "P&L Dr & Asset"], "ans": "Trading Cr & P&L Dr"},
    {"q": "58. Goods distributed as free samples are recorded as:", "options": ["Advertisement", "Purchases", "Sales", "Charity"], "ans": "Advertisement"},
    {"q": "59. Partner withdraws goods for personal use. Effects are:", "options": ["Trading Cr & Capital Dr", "Trading Dr & Capital Cr", "P&L Dr & Capital Cr", "Asset & Liability"], "ans": "Trading Cr & Capital Dr"},
    {"q": "60. Closing Stock is valued at:", "options": ["Cost or Market price, whichever is less", "Cost price always", "Market price always", "Average price"], "ans": "Cost or Market price, whichever is less"},
    {"q": "61. New RDD is calculated on:", "options": ["Net Debtors", "Gross Debtors", "Creditors", "Sales"], "ans": "Net Debtors"},
    {"q": "62. Unrecorded Sales are:", "options": ["Added to Debtors & Sales", "Deducted from Debtors", "Ignored", "Added to Creditors"], "ans": "Added to Debtors & Sales"},
    {"q": "63. Bills Receivable dishonoured:", "options": ["Add to Debtors, Less from B/R", "Less from Debtors", "Add to Creditors", "Add to Cash"], "ans": "Add to Debtors, Less from B/R"},
    {"q": "64. If New RDD is less than Old RDD, the difference is shown on:", "options": ["P&L Credit", "P&L Debit", "Asset", "Liability"], "ans": "P&L Credit"},
    {"q": "65. Reserve for discount on Debtors is calculated:", "options": ["After deducting New Bad debts & RDD", "On Gross Debtors", "Before Bad debts", "On Sales"], "ans": "After deducting New Bad debts & RDD"},
    {"q": "66. Unrecorded Purchases are:", "options": ["Added to Purchases & Creditors", "Added to Debtors", "Less from Purchases", "Less from Creditors"], "ans": "Added to Purchases & Creditors"},
    {"q": "67. Bills Payable dishonoured:", "options": ["Add to Creditors, Less from B/P", "Less from Creditors", "Add to Debtors", "Add to Sales"], "ans": "Add to Creditors, Less from B/P"},
    {"q": "68. Reserve for discount on Creditors is shown on:", "options": ["P&L Credit", "P&L Debit", "Asset", "Trading Dr"], "ans": "P&L Credit"},
    {"q": "69. Return Outward is:", "options": ["Purchase Return", "Sales Return", "Carriage", "Bad debts"], "ans": "Purchase Return"},
    {"q": "70. Return Inward is:", "options": ["Sales Return", "Purchase Return", "Freight", "Drawings"], "ans": "Sales Return"},
    {"q": "71. Under Fixed Capital, all adjustments go to:", "options": ["Current A/c", "Capital A/c", "Loan A/c", "Cash A/c"], "ans": "Current A/c"},
    {"q": "72. Under Fluctuating Capital, all adjustments go to:", "options": ["Capital A/c", "Current A/c", "Trading A/c", "P&L A/c"], "ans": "Capital A/c"},
    {"q": "73. Date of drawings not given, interest is charged for:", "options": ["6 months", "12 months", "3 months", "No interest"], "ans": "6 months"},
    {"q": "74. Interest on Partner's Loan (if silent) is:", "options": ["6% p.a.", "5% p.a.", "10% p.a.", "Not allowed"], "ans": "6% p.a."},
    {"q": "75. Interest on Capital is an ________ for the firm.", "options": ["Expense", "Income", "Asset", "Liability"], "ans": "Expense"},
    {"q": "76. Wages for installation of Machinery is added to:", "options": ["Machinery", "Wages", "Capital", "P&L"], "ans": "Machinery"},
    {"q": "77. Wages and Salaries goes to:", "options": ["Trading A/c", "Profit & Loss A/c", "Balance Sheet", "Current A/c"], "ans": "Trading A/c"},
    {"q": "78. Salaries and Wages goes to:", "options": ["Profit & Loss A/c", "Trading A/c", "Balance Sheet", "Capital A/c"], "ans": "Profit & Loss A/c"},
    {"q": "79. Trade Expenses (alone) goes to:", "options": ["Profit & Loss A/c", "Trading A/c", "Asset", "Liability"], "ans": "Profit & Loss A/c"},
    {"q": "80. Trade Expenses (with General Exp) goes to:", "options": ["Trading A/c", "Profit & Loss A/c", "Current A/c", "Balance Sheet"], "ans": "Trading A/c"},
    {"q": "81. Import Duty is debited to:", "options": ["Trading A/c", "Profit & Loss A/c", "Asset", "Capital"], "ans": "Trading A/c"},
    {"q": "82. Export Duty is debited to:", "options": ["Profit & Loss A/c", "Trading A/c", "Liability", "Capital"], "ans": "Profit & Loss A/c"},
    {"q": "83. Royalty on Production is debited to:", "options": ["Trading A/c", "Profit & Loss A/c", "Asset", "Capital"], "ans": "Trading A/c"},
    {"q": "84. Royalty on Sales is debited to:", "options": ["Profit & Loss A/c", "Trading A/c", "Liability", "Capital"], "ans": "Profit & Loss A/c"},
    {"q": "85. Import (Trading) and Export (P&L):", "options": ["True", "False", "Both Trading", "Both P&L"], "ans": "True"},
    {"q": "86. Commission received in advance is a:", "options": ["Liability", "Asset", "Income", "Expense"], "ans": "Liability"},
    {"q": "87. Interest on Investment due but not received is a:", "options": ["Asset", "Liability", "Expense", "Loss"], "ans": "Asset"},
    {"q": "88. Outstanding Rent is a:", "options": ["Liability", "Asset", "Capital", "Expense"], "ans": "Liability"},
    {"q": "89. Prepaid Insurance is a:", "options": ["Asset", "Liability", "Income", "Expense"], "ans": "Asset"},
    {"q": "90. Loss on sale of Asset is debited to:", "options": ["Profit & Loss A/c", "Trading A/c", "Asset A/c", "Capital A/c"], "ans": "Profit & Loss A/c"},
    {"q": "91. COGS = Op Stock + Purchase + Direct Exp - Closing Stock:", "options": ["True", "False", "Only Op Stock", "Only Purchase"], "ans": "True"},
    {"q": "92. Gross Profit = Sales - COGS:", "options": ["True", "False", "Sales + COGS", "COGS - Sales"], "ans": "True"},
    {"q": "93. Operating Profit = GP - Operating Expenses:", "options": ["True", "False", "GP + Expenses", "Net Profit"], "ans": "True"},
    {"q": "94. Partner's Commission on Net Profit is debited to:", "options": ["Profit & Loss A/c", "Trading A/c", "Balance Sheet", "Asset"], "ans": "Profit & Loss A/c"},
    {"q": "95. Depreciation is charged on:", "options": ["Fixed Assets", "Current Assets", "Only Cash", "Only Debtors"], "ans": "Fixed Assets"},
    {"q": "96. Partnership Registration is compulsory in Maharashtra:", "options": ["True", "False", "Optional", "Only for big firms"], "ans": "True"},
    {"q": "97. No agreement, profits shared equally:", "options": ["True", "False", "In Capital ratio", "In Time ratio"], "ans": "True"},
    {"q": "98. Maximum partners in a firm are:", "options": ["50", "20", "100", "Unlimited"], "ans": "50"},
    {"q": "99. Balance Sheet is a Statement:", "options": ["True", "False", "It is an Account", "It is a Ledger"], "ans": "True"},
    {"q": "100. Goodwill is an Intangible Asset:", "options": ["True", "False", "Tangible", "Fictitious"], "ans": "True"}
]

# --- CHAPTER 2: NOT FOR PROFIT CONCERNS (NPO) (100 Qs) ---
quiz_data_npo = [
    {"q": "1. NPO is established for:", "options": ["Services", "Profit", "Trading", "Dividend"], "ans": "Services"},
    {"q": "2. Example of NPO is:", "options": ["Schools/Hospitals", "Reliance", "Tata", "Shop"], "ans": "Schools/Hospitals"},
    {"q": "3. Main income of NPO is:", "options": ["Subscription", "Sales", "Gross Profit", "Capital"], "ans": "Subscription"},
    {"q": "4. Receipts & Payments A/c is a summary of:", "options": ["Cash Book", "Pass Book", "Ledger", "Balance Sheet"], "ans": "Cash Book"},
    {"q": "5. Receipts & Payments A/c is a __________ Account:", "options": ["Real", "Nominal", "Personal", "Capital"], "ans": "Real"},
    {"q": "6. Income & Expenditure A/c is a __________ Account:", "options": ["Nominal", "Real", "Personal", "Asset"], "ans": "Nominal"},
    {"q": "7. Income & Expenditure A/c shows:", "options": ["Surplus/Deficit", "Net Profit", "Cash balance", "Capital"], "ans": "Surplus/Deficit"},
    {"q": "8. Receipts are recorded on the __________ side:", "options": ["Debit", "Credit", "Asset", "Liability"], "ans": "Debit"},
    {"q": "9. Incomes are recorded on the __________ side:", "options": ["Credit", "Debit", "Liability", "Asset"], "ans": "Credit"},
    {"q": "10. Income & Expenditure A/c is on __________ basis:", "options": ["Accrual", "Cash", "Mixed", "Single"], "ans": "Accrual"},
    {"q": "11. Only __________ items are in I&E A/c:", "options": ["Revenue", "Capital", "Deferred", "Both"], "ans": "Revenue"},
    {"q": "12. Receipts & Payments A/c records __________ items:", "options": ["Both Capital & Revenue", "Only Capital", "Only Revenue", "None"], "ans": "Both Capital & Revenue"},
    {"q": "13. Outstanding subscription (current year) is an:", "options": ["Asset", "Liability", "Expense", "Loss"], "ans": "Asset"},
    {"q": "14. Subscription received in advance is a:", "options": ["Liability", "Asset", "Income", "Expense"], "ans": "Liability"},
    {"q": "15. Periodic payment by members is called:", "options": ["Subscription", "Donation", "Legacy", "Entrance Fee"], "ans": "Subscription"},
    {"q": "16. Entrance fees are generally __________:", "options": ["Revenue", "Capital", "Asset", "Liability"], "ans": "Revenue"},
    {"q": "17. Legacies are generally __________:", "options": ["Capitalised", "Revenue", "Expense", "Deducted"], "ans": "Capitalised"},
    {"q": "18. Specific Donation is shown as:", "options": ["Liability", "Asset", "Income", "Expense"], "ans": "Liability"},
    {"q": "19. General Donation is treated as:", "options": ["Revenue Income", "Capital", "Liability", "Asset"], "ans": "Revenue Income"},
    {"q": "20. Life Membership Fees are __________:", "options": ["Capital Receipt", "Revenue", "Expense", "Short-term"], "ans": "Capital Receipt"},
    {"q": "21. Sale of old newspapers is:", "options": ["Revenue Receipt", "Capital", "Liability", "Asset"], "ans": "Revenue Receipt"},
    {"q": "22. Profit on sale of Asset is credited to:", "options": ["Income & Expenditure A/c", "Receipts A/c", "Capital Fund", "Asset A/c"], "ans": "Income & Expenditure A/c"},
    {"q": "23. Loss on sale of Asset is debited to:", "options": ["Income & Expenditure A/c", "Capital Fund", "Asset A/c", "Cash A/c"], "ans": "Income & Expenditure A/c"},
    {"q": "24. Depreciation is a __________ expense:", "options": ["Non-cash", "Cash", "Capital", "Personal"], "ans": "Non-cash"},
    {"q": "25. Depreciation in NPO is debited to:", "options": ["Income & Expenditure A/c", "Receipts A/c", "Trading A/c", "Capital"], "ans": "Income & Expenditure A/c"},
    {"q": "26. Honorarium paid is __________ payment:", "options": ["Revenue", "Capital", "Asset", "Liability"], "ans": "Revenue"},
    {"q": "27. Purchase of Sports Equipment is __________:", "options": ["Capital Expenditure", "Revenue", "Expense", "Liability"], "ans": "Capital Expenditure"},
    {"q": "28. Excess of Income over Expenditure is:", "options": ["Surplus", "Deficit", "Net Profit", "Net Loss"], "ans": "Surplus"},
    {"q": "29. Excess of Expenditure over Income is:", "options": ["Deficit", "Surplus", "Net Loss", "Net Profit"], "ans": "Deficit"},
    {"q": "30. Surplus is __________ to Capital Fund:", "options": ["Added", "Deducted", "Ignored", "Asset"], "ans": "Added"},
    {"q": "31. Deficit is __________ from Capital Fund:", "options": ["Deducted", "Added", "Ignored", "Liability"], "ans": "Deducted"},
    {"q": "32. Capital Fund = Total Assets - Total Liabilities:", "options": ["True", "False", "Assets + Liabilities", "Income - Exp"], "ans": "True"},
    {"q": "33. Opening Balance Sheet gives:", "options": ["Capital Fund", "Cash balance", "Surplus", "Deficit"], "ans": "Capital Fund"},
    {"q": "34. Opening cash is on __________ of R&P A/c:", "options": ["Debit side", "Credit side", "Asset", "Liability"], "ans": "Debit side"},
    {"q": "35. R&P Credit balance at end means:", "options": ["Bank Overdraft", "Cash in hand", "Capital", "Asset"], "ans": "Bank Overdraft"},
    {"q": "36. Which is NOT in I&E A/c?", "options": ["Purchase of furniture", "Salaries", "Rent", "Depreciation"], "ans": "Purchase of furniture"},
    {"q": "37. Repairs to old building is:", "options": ["Revenue Expenditure", "Capital", "Asset", "Liability"], "ans": "Revenue Expenditure"},
    {"q": "38. Building construction is:", "options": ["Capital Expenditure", "Revenue", "Income", "Liability"], "ans": "Capital Expenditure"},
    {"q": "39. Tournament Fund is a:", "options": ["Liability", "Asset", "Income", "Expense"], "ans": "Liability"},
    {"q": "40. Tournament Expenses are deducted from:", "options": ["Tournament Fund", "I&E A/c", "Capital Fund", "Cash"], "ans": "Tournament Fund"},
    {"q": "41. Outstanding expenses are __________ to expense:", "options": ["Added", "Deducted", "Ignored", "Asset"], "ans": "Added"},
    {"q": "42. Prepaid expenses are __________ from expense:", "options": ["Deducted", "Added", "Ignored", "Liability"], "ans": "Deducted"},
    {"q": "43. Prev year O/S subscription received is __________:", "options": ["Deducted", "Added", "Ignored", "Asset"], "ans": "Deducted"},
    {"q": "44. Prev year advance for Current year is __________:", "options": ["Added", "Deducted", "Ignored", "Liability"], "ans": "Added"},
    {"q": "45. Stationery Consumed = Op + Purchase - Cl Stock:", "options": ["True", "False", "Op - Purchase", "Purchase - Cl"], "ans": "True"},
    {"q": "46. Stock of stationery at end is an:", "options": ["Asset", "Liability", "Income", "Expense"], "ans": "Asset"},
    {"q": "47. Specific Govt Grant is a:", "options": ["Capital Receipt", "Revenue", "Income", "Expense"], "ans": "Capital Receipt"},
    {"q": "48. Endowment Fund is __________:", "options": ["Capital Receipt", "Revenue", "Recurring", "Minor"], "ans": "Capital Receipt"},
    {"q": "49. R&P A/c is like Cash Book:", "options": ["True", "False", "Like Trial Balance", "Like P&L"], "ans": "True"},
    {"q": "50. I&E A/c is like Profit & Loss A/c:", "options": ["True", "False", "Like Cash Book", "Like Trading"], "ans": "True"},
    {"q": "51. NPOs do not prepare Trading A/c:", "options": ["True", "False", "Only big ones", "Sometimes"], "ans": "True"},
    {"q": "52. Specific Fund expense is deducted from that Fund:", "options": ["True", "False", "I&E Debit", "I&E Credit"], "ans": "True"},
    {"q": "53. Income from specific fund investment is added to Fund:", "options": ["True", "False", "I&E Credit", "Capital Fund"], "ans": "True"},
    {"q": "54. 50% Entrance Fees capitalised, rest is Revenue:", "options": ["True", "False", "Rest is Asset", "Rest is Liability"], "ans": "True"},
    {"q": "55. Non-cash items are NOT in R&P A/c:", "options": ["True", "False", "They are in it", "Sometimes"], "ans": "True"},
    {"q": "56. Locker Rent is Revenue Receipt:", "options": ["True", "False", "Capital", "Liability"], "ans": "True"},
    {"q": "57. Books for Library is Capital Expenditure:", "options": ["True", "False", "Revenue", "Asset Liability"], "ans": "True"},
    {"q": "58. Prize Fund 10k, Prize 12k. 2k extra to I&E Debit:", "options": ["True", "False", "To Capital Fund", "To Asset"], "ans": "True"},
    {"q": "59. Billiard Table is an Asset:", "options": ["True", "False", "Expense", "Liability"], "ans": "True"},
    {"q": "60. Capital Fund is also General Fund:", "options": ["True", "False", "Endowment", "Prize Fund"], "ans": "True"},
    {"q": "61. Current year O/S Rent is a Liability:", "options": ["True", "False", "Asset", "Capital"], "ans": "True"},
    {"q": "62. Prev year O/S sub in Op. B/S is an Asset:", "options": ["True", "False", "Liability", "Debit of I&E"], "ans": "True"},
    {"q": "63. Prev year advance sub in Op. B/S is a Liability:", "options": ["True", "False", "Asset", "Capital"], "ans": "True"},
    {"q": "64. Cl stock of Medicine is an Asset:", "options": ["True", "False", "Liability", "Income"], "ans": "True"},
    {"q": "65. Sale of old sports material is Revenue Income:", "options": ["True", "False", "Capital", "Liability"], "ans": "True"},
    {"q": "66. Loss on sale of furniture to I&E Debit:", "options": ["True", "False", "To Capital Fund", "To Asset"], "ans": "True"},
    {"q": "67. Op. Cash/Bank in R&P is balance at beginning:", "options": ["True", "False", "At end", "At middle"], "ans": "True"},
    {"q": "68. Cl. balance of R&P to Cl. Balance Sheet:", "options": ["True", "False", "To I&E", "To Capital Fund"], "ans": "True"},
    {"q": "69. Legacies as Revenue goes to I&E Credit:", "options": ["True", "False", "To Capital Fund", "To Asset"], "ans": "True"},
    {"q": "70. Capitalised Entrance Fees to Capital Fund:", "options": ["True", "False", "I&E Debit", "I&E Credit"], "ans": "True"},
    {"q": "71. Bank interest is Revenue Income:", "options": ["True", "False", "Capital", "Liability"], "ans": "True"},
    {"q": "72. Deficit = Exp > Income:", "options": ["True", "False", "Income > Exp", "Asset > Liab"], "ans": "True"},
    {"q": "73. Surplus = Income > Exp:", "options": ["True", "False", "Exp > Income", "Liab > Asset"], "ans": "True"},
    {"q": "74. Donation for Pavilion is Capital Receipt:", "options": ["True", "False", "Revenue", "Asset"], "ans": "True"},
    {"q": "75. Salary 5k (1k prev year). 4k is current exp:", "options": ["True", "False", "6k", "5k"], "ans": "True"},
    {"q": "76. Sub 10k (2k next year). 8k is current income:", "options": ["True", "False", "12k", "10k"], "ans": "True"},
    {"q": "77. Library Books is Capital Exp:", "options": ["True", "False", "Revenue", "Loss"], "ans": "True"},
    {"q": "78. Municipal taxes is Revenue Exp:", "options": ["True", "False", "Capital", "Asset"], "ans": "True"},
    {"q": "79. R&P A/c does not separate Cap/Rev:", "options": ["True", "False", "It separates", "Only Rev"], "ans": "True"},
    {"q": "80. I&E A/c records only current year:", "options": ["True", "False", "All years", "Next year"], "ans": "True"},
    {"q": "81. NPO prepares Final Accounts at end:", "options": ["True", "False", "Only cash book", "Monthly"], "ans": "True"},
    {"q": "82. Match Fund 50k, Exp 40k. 10k is Liability:", "options": ["True", "False", "Asset", "Income"], "ans": "True"},
    {"q": "83. Fixed Deposit is an Asset:", "options": ["True", "False", "Expense", "Liability"], "ans": "True"},
    {"q": "84. Sale of old periodicals is Revenue Income:", "options": ["True", "False", "Capital", "Asset"], "ans": "True"},
    {"q": "85. Profit on machinery sale to I&E Credit:", "options": ["True", "False", "To Machinery", "Capital Fund"], "ans": "True"},
    {"q": "86. Building depreciation to I&E Debit:", "options": ["True", "False", "To Building", "Ignored"], "ans": "True"},
    {"q": "87. Capital Fund = Assets - Ext. Liab:", "options": ["True", "False", "Income - Exp", "Cash - Bank"], "ans": "True"},
    {"q": "88. Endowment Fund is a Liability:", "options": ["True", "False", "Asset", "Revenue Income"], "ans": "True"},
    {"q": "89. Income due but not received is Accrued Income:", "options": ["True", "False", "Unearned", "Deficit"], "ans": "True"},
    {"q": "90. O/S subscription 500 is an Asset:", "options": ["True", "False", "Liability", "Capital"], "ans": "True"},
    {"q": "91. Rent paid in advance 1000 is an Asset:", "options": ["True", "False", "Liability", "Capital"], "ans": "True"},
    {"q": "92. Subscription in advance 2000 is a Liability:", "options": ["True", "False", "Asset", "Capital"], "ans": "True"},
    {"q": "93. Honorarium to Doctor is Revenue Exp:", "options": ["True", "False", "Capital", "Asset"], "ans": "True"},
    {"q": "94. Govt Bonds is an Investment (Asset):", "options": ["True", "False", "Expense", "Revenue Receipt"], "ans": "True"},
    {"q": "95. Special Subscription for Party to separate Fund:", "options": ["True", "False", "I&E Credit", "I&E Debit"], "ans": "True"},
    {"q": "96. Drugs consumed = 2k op + 10k pur - 3k cl = 9k:", "options": ["True", "False", "12k", "15k"], "ans": "True"},
    {"q": "97. Assets 5L, Liab 1k. Cap Fund 4L:", "options": ["True", "False", "6L", "5L"], "ans": "True"},
    {"q": "98. Deficit 20k, Cap Fund 1L. Cl. Fund 80k:", "options": ["True", "False", "1.2L", "1L"], "ans": "True"},
    {"q": "99. NPO has Capital Fund, not Capital A/c:", "options": ["True", "False", "Drawings", "Loan"], "ans": "True"},
    {"q": "100. R&P balance is Cash/Bank Balance:", "options": ["True", "False", "Surplus", "Net Profit"], "ans": "True"}
]

# --- CHAPTER 3: ADMISSION OF PARTNER (100 Qs) ---
quiz_data_admission = [
    {"q": "1. When a new partner is admitted, old partnership is:", "options": ["Dissolved", "Continued", "Reconstituted", "Liquidated"], "ans": "Reconstituted"},
    {"q": "2. Ratio in which old partners surrender their share is:", "options": ["New Ratio", "Gaining Ratio", "Sacrificing Ratio", "Capital Ratio"], "ans": "Sacrificing Ratio"},
    {"q": "3. Formula for Sacrificing Ratio:", "options": ["New - Old", "Old - New", "Old - Gaining", "New - Gaining"], "ans": "Old - New"},
    {"q": "4. Account to record revaluation of assets & liabilities:", "options": ["P&L A/c", "Realisation A/c", "Revaluation A/c", "Capital A/c"], "ans": "Revaluation A/c"},
    {"q": "5. Revaluation Account is a __________ account:", "options": ["Personal", "Real", "Nominal", "Bank"], "ans": "Nominal"},
    {"q": "6. Increase in asset value is __________ to Revaluation A/c:", "options": ["Credited", "Debited", "Ignored", "Added to Capital"], "ans": "Credited"},
    {"q": "7. Decrease in liability value is a __________:", "options": ["Loss", "Gain (Profit)", "Expense", "Asset"], "ans": "Gain (Profit)"},
    {"q": "8. Unrecorded liabilities are __________ to Revaluation A/c:", "options": ["Debited", "Credited", "Ignored", "Asset"], "ans": "Debited"},
    {"q": "9. Profit on Revaluation is transferred to:", "options": ["All partners", "New partner", "Old Partners", "None"], "ans": "Old Partners"},
    {"q": "10. Revaluation balance shared by old partners in their:", "options": ["New Ratio", "Old Ratio", "Sacrificing Ratio", "Capital Ratio"], "ans": "Old Ratio"},
    {"q": "11. Goodwill in cash by new partner is __________ method:", "options": ["Valuation", "Premium", "Average", "Super"], "ans": "Premium"},
    {"q": "12. Cash goodwill is credited to __________ A/c:", "options": ["Premium for Goodwill", "Cash", "New Partner", "Revaluation"], "ans": "Premium for Goodwill"},
    {"q": "13. New partner's goodwill is shared by old partners in:", "options": ["Old Ratio", "New Ratio", "Capital Ratio", "Sacrificing Ratio"], "ans": "Sacrificing Ratio"},
    {"q": "14. If old partners withdraw goodwill, __________ A/c is debited:", "options": ["Cash", "Old Partners Capital", "Goodwill", "Revaluation"], "ans": "Old Partners Capital"},
    {"q": "15. Goodwill raised in books credits __________ A/c:", "options": ["Cash", "Goodwill", "Old Partners Capital", "New Partner"], "ans": "Old Partners Capital"},
    {"q": "16. Raised goodwill is shared by old partners in:", "options": ["Old Ratio", "New Ratio", "Sacrificing Ratio", "Equal"], "ans": "Old Ratio"},
    {"q": "17. Goodwill written off is debited to __________ partners:", "options": ["Old", "New", "All", "Continuing"], "ans": "All"},
    {"q": "18. General Reserve in old B/S is transferred to:", "options": ["All partners", "Old Partners Capital", "Revaluation", "Cash"], "ans": "Old Partners Capital"},
    {"q": "19. General Reserve distributed in __________ ratio:", "options": ["Sacrificing", "New", "Old", "Equal"], "ans": "Old Ratio"},
    {"q": "20. Accumulated losses are __________ to old partners:", "options": ["Debited", "Credited", "Ignored", "Added"], "ans": "Debited"},
    {"q": "21. New Ratio = Old Ratio - Sacrificing Ratio:", "options": ["True", "False", "Old + Sacrifice", "Old / New"], "ans": "True"},
    {"q": "22. New partner brings capital in assets, entry debits:", "options": ["Cash", "Assets", "Capital", "Revaluation"], "ans": "Assets"},
    {"q": "23. Workmen Compensation Reserve is an __________:", "options": ["Asset", "Accumulated Profit", "Expense", "External Liability"], "ans": "Accumulated Profit"},
    {"q": "24. Unrecorded asset discovered is __________ to Revaluation A/c:", "options": ["Debited", "Credited", "Asset", "Cash"], "ans": "Credited"},
    {"q": "25. Creating RDD on debtors is a __________:", "options": ["Profit", "Loss", "Liability", "Capital"], "ans": "Loss"},
    {"q": "26. Cash brought for goodwill, debit goes to:", "options": ["Premium A/c", "Cash/Bank A/c", "Capital A/c", "Revaluation A/c"], "ans": "Cash/Bank A/c"},
    {"q": "27. General Reserve to old partners is correct:", "options": ["True", "False", "To all partners", "To new only"], "ans": "True"},
    {"q": "28. Employees' Provident Fund is a __________:", "options": ["Profit", "Reserve", "Liability", "Asset"], "ans": "Liability"},
    {"q": "29. New partner brings cash capital, credit goes to:", "options": ["Old Partners", "Revaluation", "New Partner Capital", "Cash"], "ans": "New Partner Capital"},
    {"q": "30. Machinery appreciated by 10%, credit goes to:", "options": ["Machinery", "Revaluation A/c", "Old Partners", "Cash"], "ans": "Revaluation A/c"},
    {"q": "31. Building depreciated, debit goes to:", "options": ["Revaluation A/c", "Building A/c", "Old Partners", "Suspense"], "ans": "Revaluation A/c"},
    {"q": "32. O/S Expenses on admission decreases profit:", "options": ["True", "False", "Increases", "No effect"], "ans": "True"},
    {"q": "33. Prepaid insurance on admission credits Revaluation:", "options": ["True", "False", "Debits", "Ignored"], "ans": "True"},
    {"q": "34. Sacrificing = Old - New:", "options": ["True", "False", "New - Old", "Old + New"], "ans": "True"},
    {"q": "35. Partner 50k capital for 1/4 share, total capital is:", "options": ["1L", "1.5L", "2L", "50k"], "ans": "2L"},
    {"q": "36. Partners withdraw goodwill, credit goes to:", "options": ["Old Partners", "Cash/Bank A/c", "Revaluation", "Goodwill"], "ans": "Cash/Bank A/c"},
    {"q": "37. Accumulated Losses shared in Old Ratio:", "options": ["True", "False", "New Ratio", "Sacrifice Ratio"], "ans": "True"},
    {"q": "38. P&L Debit balance is Accumulated Loss:", "options": ["True", "False", "Profit", "Liability"], "ans": "True"},
    {"q": "39. Revaluation A/c is P&L Adjustment A/c:", "options": ["True", "False", "Realisation", "Trading"], "ans": "True"},
    {"q": "40. Creditor accepting less is a Gain:", "options": ["True", "False", "Loss", "Liability"], "ans": "True"},
    {"q": "41. Provision for discount on creditors increases profit:", "options": ["True", "False", "Decreases", "No effect"], "ans": "True"},
    {"q": "42. Unrecorded investment found credits Revaluation:", "options": ["True", "False", "Debits", "Ignored"], "ans": "True"},
    {"q": "43. New partner capital by agreement is correct:", "options": ["True", "False", "By law", "By bank"], "ans": "True"},
    {"q": "44. Writing off goodwill debits all in New Ratio:", "options": ["True", "False", "Old Ratio", "Sacrifice Ratio"], "ans": "True"},
    {"q": "45. Goodwill paid privately, no firm entry:", "options": ["True", "False", "Debit Cash", "Debit Capital"], "ans": "True"},
    {"q": "46. Investment Fluctuation Reserve is specific:", "options": ["True", "False", "Free reserve", "Liability"], "ans": "True"},
    {"q": "47. IFR to old partners if book = market value:", "options": ["True", "False", "To Revaluation", "To New partner"], "ans": "True"},
    {"q": "48. Contingency Reserve in Old Ratio:", "options": ["True", "False", "New Ratio", "Sacrifice Ratio"], "ans": "True"},
    {"q": "49. Stock undervalued credits Revaluation:", "options": ["True", "False", "Debits", "Ignored"], "ans": "True"},
    {"q": "50. Building overvalued debits Revaluation:", "options": ["True", "False", "Credits", "Ignored"], "ans": "True"},
    {"q": "51. Capital A/c balance is Closing Capital:", "options": ["True", "False", "Profit", "Goodwill"], "ans": "True"},
    {"q": "52. O/S expense is NOT an unrecorded asset:", "options": ["True", "False", "It is asset", "It is income"], "ans": "True"},
    {"q": "53. Decrease in RDD is profit on revaluation:", "options": ["True", "False", "Loss", "Liability"], "ans": "True"},
    {"q": "54. No cash goodwill is Valuation Method:", "options": ["True", "False", "Premium", "Average"], "ans": "True"},
    {"q": "55. Sacrifice ratio for cash goodwill:", "options": ["True", "False", "Old ratio", "New ratio"], "ans": "True"},
    {"q": "56. Capital adjustment through Cash/Current A/c:", "options": ["True", "False", "Revaluation", "P&L"], "ans": "True"},
    {"q": "57. Admission needs consent of all partners:", "options": ["True", "False", "Majority only", "No consent"], "ans": "True"},
    {"q": "58. Admission requires change in Deed:", "options": ["True", "False", "Cash Book", "Trading A/c"], "ans": "True"},
    {"q": "59. New partner shares future profits & assets:", "options": ["True", "False", "Only profit", "Past profit"], "ans": "True"},
    {"q": "60. AS 26 deals with Intangible assets:", "options": ["True", "False", "AS 10", "AS 2"], "ans": "True"},
    {"q": "61. Goodwill 30k, 1/3 share = 10k cash:", "options": ["True", "False", "30k", "20k"], "ans": "True"},
    {"q": "62. New capital based on share & total capital:", "options": ["True", "False", "On age", "On cash"], "ans": "True"},
    {"q": "63. New partner share surrendered by old partners:", "options": ["True", "False", "Creditors", "Bank"], "ans": "True"},
    {"q": "64. Revaluation profit belongs to Old Partners:", "options": ["True", "False", "All partners", "New only"], "ans": "True"},
    {"q": "65. New B/S has revised values:", "options": ["True", "False", "Old values", "Only new"], "ans": "True"},
    {"q": "66. Retained earnings shared in Old Ratio:", "options": ["True", "False", "New Ratio", "Sacrifice"], "ans": "True"},
    {"q": "67. Provision for discount on debtors is a loss:", "options": ["True", "False", "Gain", "Asset"], "ans": "True"},
    {"q": "68. Bad debts recovered is a gain:", "options": ["True", "False", "Loss", "Expense"], "ans": "True"},
    {"q": "69. Workmen claim < reserve, credits old partners:", "options": ["True", "False", "Debits", "Ignored"], "ans": "True"},
    {"q": "70. Undistributed losses on Asset side:", "options": ["True", "False", "Liability", "P&L Credit"], "ans": "True"},
    {"q": "71. Revaluation closed to Old Partners Capital:", "options": ["True", "False", "New Partner", "Cash"], "ans": "True"},
    {"q": "72. Cash/Bank shows actual cash position:", "options": ["True", "False", "Revaluation", "Capital"], "ans": "True"},
    {"q": "73. Old goodwill in B/S written off in Old Ratio:", "options": ["True", "False", "New Ratio", "New partner"], "ans": "True"},
    {"q": "74. Old goodwill write off: Old Partners Dr to Goodwill:", "options": ["True", "False", "Goodwill to Old Partners", "P&L to Goodwill"], "ans": "True"},
    {"q": "75. Sacrifice + New = Old Ratio:", "options": ["True", "False", "Gaining Ratio", "Capital Ratio"], "ans": "True"},
    {"q": "76. GP over debit in Revaluation is Profit:", "options": ["True", "False", "Loss", "Deficit"], "ans": "True"},
    {"q": "77. Debit over credit in Revaluation is Loss:", "options": ["True", "False", "Profit", "Surplus"], "ans": "True"},
    {"q": "78. Capital brings right over Assets:", "options": ["True", "False", "Profits", "Liabilities"], "ans": "True"},
    {"q": "79. Goodwill brings right over Future Profits:", "options": ["True", "False", "Assets", "Liabilities"], "ans": "True"},
    {"q": "80. No cash goodwill adjusted to Current/Capital A/c:", "options": ["True", "False", "Cash A/c", "Revaluation"], "ans": "True"},
    {"q": "81. P&L Debit is NOT accumulated profit:", "options": ["True", "False", "Gen Reserve", "WCR"], "ans": "True"},
    {"q": "82. Revaluation expenses debit Revaluation A/c:", "options": ["True", "False", "Cash A/c", "Capital A/c"], "ans": "True"},
    {"q": "83. After transfer, Revaluation balance is Nil:", "options": ["True", "False", "Debit bal", "Credit bal"], "ans": "True"},
    {"q": "84. Decrease in asset is a Loss:", "options": ["True", "False", "Profit", "Reserve"], "ans": "True"},
    {"q": "85. Increase in liability is a Loss:", "options": ["True", "False", "Profit", "Asset"], "ans": "True"},
    {"q": "86. Unrecorded asset taken by partner, debits his Capital:", "options": ["True", "False", "Credits", "No effect"], "ans": "True"},
    {"q": "87. Unrecorded liability paid credits Cash/Bank:", "options": ["True", "False", "Credits Revaluation", "Credits Capital"], "ans": "True"},
    {"q": "88. Goodwill raised at full value debits Goodwill A/c:", "options": ["True", "False", "Premium A/c", "Revaluation"], "ans": "True"},
    {"q": "89. Old Ratio equal, 1/4 share, Sacrifice Ratio 1:1:", "options": ["True", "False", "1:2", "3:1"], "ans": "True"},
    {"q": "90. Accumulated losses debited to Old Partners:", "options": ["True", "False", "Credited", "To Asset side"], "ans": "True"},
    {"q": "91. Cash capital increases total capital of firm:", "options": ["True", "False", "Decreases", "No effect"], "ans": "True"},
    {"q": "92. Capital adjustment goes to Cash/Current A/c:", "options": ["True", "False", "Revaluation", "Goodwill"], "ans": "True"},
    {"q": "93. Values not changed, use Memo Revaluation A/c:", "options": ["True", "False", "Revaluation", "Realisation"], "ans": "True"},
    {"q": "94. Purpose of admission is Capital & Skill:", "options": ["True", "False", "To dissolve", "To increase liab"], "ans": "True"},
    {"q": "95. Revaluation at Admission/Retirement/Death:", "options": ["True", "False", "Only Admission", "Only Retirement"], "ans": "True"},
    {"q": "96. New Cash = Op + Cap in + Goodwill in:", "options": ["True", "False", "Op - Cap", "Only Cap"], "ans": "True"},
    {"q": "97. Unrecorded WCR liability debits Revaluation:", "options": ["True", "False", "Credits", "Ignored"], "ans": "True"},
    {"q": "98. Old Bad debts recovered credits Revaluation:", "options": ["True", "False", "Debits", "Less from Debtors"], "ans": "True"},
    {"q": "99. Fluctuating capital adjustments in Capital A/c:", "options": ["True", "False", "Current A/c", "Revaluation"], "ans": "True"},
    {"q": "100. Final balance is Closing Capital of firm:", "options": ["True", "False", "Loss", "Goodwill"], "ans": "True"}
]

# -----------------------------------------------------
# ३. वेबसाईटचे डिझाईन आणि मेनू बार (Menu Bar)
# -----------------------------------------------------
st.set_page_config(page_title="Mukesh Sir's Online Exam", page_icon="📝")

st.sidebar.title("📚 Mitradnya Publication's Online Exam")
st.sidebar.markdown("---")

# --- धडा निवडण्याची सिस्टीम (Chapter Selection) ---
st.sidebar.subheader("1. Select Chapter:")
selected_chapter = st.sidebar.selectbox("Choose a Subject / Topic:", [
    "Chapter 1: Partnership Final Accounts",
    "Chapter 2: Not for Profit Concerns (NPO)",
    "Chapter 3: Admission of Partner"
])

# --- निवडलेल्या धड्यानुसार प्रश्न बाहेर काढण्याची सिस्टीम ---
if selected_chapter == "Chapter 1: Partnership Final Accounts":
    active_quiz_data = quiz_data_partnership
elif selected_chapter == "Chapter 2: Not for Profit Concerns (NPO)":
    active_quiz_data = quiz_data_npo
else:
    active_quiz_data = quiz_data_admission

st.sidebar.markdown("---")

# --- टेस्ट पार्ट निवडण्याची सिस्टीम ---
st.sidebar.subheader("2. Select Test Part:")
test_choice = st.sidebar.radio("Choose Questions:", [
    "Test 1: Part 1 (Q1-Q25)",
    "Test 2: Part 2 (Q26-Q50)",
    "Test 3: Part 3 (Q51-Q75)",
    "Test 4: Part 4 (Q76-Q100)"
])
st.sidebar.markdown("---")
st.sidebar.info("Developed by Mukesh Sir (9130103386)")

if test_choice == "Test 1: Part 1 (Q1-Q25)":
    current_quiz = active_quiz_data[0:25]
    topic_name = "Part 1 (Q1-Q25)"
elif test_choice == "Test 2: Part 2 (Q26-Q50)":
    current_quiz = active_quiz_data[25:50]
    topic_name = "Part 2 (Q26-Q50)"
elif test_choice == "Test 3: Part 3 (Q51-Q75)":
    current_quiz = active_quiz_data[50:75]
    topic_name = "Part 3 (Q51-Q75)"
else:
    current_quiz = active_quiz_data[75:100]
    topic_name = "Part 4 (Q76-Q100)"

st.title("📚 Mukesh Sir's - Online Exam 📚")
st.subheader(f"Topic: {selected_chapter}")
st.markdown(f"**Test: {topic_name} (25 Marks)**")

st.markdown("---")
student_name = st.text_input("👤 Enter Your Full Name:")
student_division = st.text_input("🏫 Enter Your Division (e.g., A, B, C):")
student_roll_no = st.text_input("🔢 Enter Your Roll No:")
student_email = st.text_input("📧 Enter Your Email ID (To Get Result on Mail):") 
st.markdown("---")

user_answers = []

for index, item in enumerate(current_quiz):
    st.markdown(f"**{item['q']}**")
    ans = st.radio("Options:", item['options'], key=f"test_{selected_chapter}_{test_choice}_q_{index}", label_visibility="collapsed", index=None)
    user_answers.append(ans)
    st.markdown("<br>", unsafe_allow_html=True)

st.markdown("---")

# सबमिट बटण आणि तपासणी
if st.button("🚀 Submit Exam"):
    if student_name == "" or student_division == "" or student_roll_no == "":
        st.warning("⚠️ Please enter your Name, Division, and Roll No first!")
    elif None in user_answers:
        st.warning("⚠️ Please answer all questions before submitting!")
    else:
        score = 0
        total_questions = len(current_quiz)
        report_text = "" 
        
        for i in range(total_questions):
            if user_answers[i] == current_quiz[i]['ans']:
                score += 1
                
        # १. मुख्य निकाल दाखवणे
        st.success(f"🎉 Exam Submitted! Dear {student_name}, your Score is {score}/{total_questions}")
        
        # २. Google Sheet मध्ये अचूक डेटा पाठवणे 
        with st.spinner("Saving data to Mitradnya Excel..."):
            GOOGLE_SHEET_URL = "https://script.google.com/macros/s/AKfycbw7BoAF9_uf5pp1kM7XhpsIGb7zfMeX708BAFTjuoDLCUK4Yhpm-kbX2TevEeB_K5Yq/exec"
            
            try:
                safe_name = urllib.parse.quote(student_name)
                safe_div = urllib.parse.quote(student_division)
                safe_roll = urllib.parse.quote(student_roll_no)
                full_test_name = f"{selected_chapter} - {topic_name}"
                safe_test = urllib.parse.quote(full_test_name)
                safe_score = urllib.parse.quote(f"{score}/{total_questions}")
                
                final_url = f"{GOOGLE_SHEET_URL}?name={safe_name}&div={safe_div}&roll={safe_roll}&test={safe_test}&score={safe_score}"
                
                res = requests.get(final_url)
                if res.status_code == 200:
                    st.info("📊 Data successfully added to your Excel report.")
                else:
                    st.error(f"Google Sheet Error: Status Code {res.status_code}")
            except Exception as e:
                st.error(f"Data saving failed Error: {e}")

        st.markdown("---")
        st.markdown("### 📊 तुमचा सविस्तर निकाल (Detailed Report):")
        
        for i in range(total_questions):
            user_ans = user_answers[i]
            correct_ans = current_quiz[i]['ans']
            question_text = current_quiz[i]['q']
            
            if user_ans == correct_ans:
                st.success(f"**{question_text}**\n\n✅ Your Ans: {user_ans}")
                report_text += f"{question_text}\n✅ Your Ans: {user_ans} (Correct)\n\n"
            else:
                st.error(f"**{question_text}**\n\n❌ Your Ans: {user_ans} \n\n🎯 Correct Ans: {correct_ans}")
                report_text += f"{question_text}\n❌ Your Ans: {user_ans} \n🎯 Correct Ans: {correct_ans}\n\n"
        
        # ४. ईमेल पाठवण्याची सिस्टीम
        with st.spinner("Saving Result..."):
            send_score_to_teacher(student_name, student_division, student_roll_no, score, total_questions, selected_chapter, topic_name)
            
            if student_email != "":
                try:
                    student_msg = MIMEText(f"Dear {student_name},\n\nYour Score for {selected_chapter} ({topic_name}) is {score}/{total_questions}.\n\nBelow is your detailed report:\n\n{report_text}\n\nKeep Studying!\n- Mukesh Arvind Amrutkar (9130103386)")
                    student_msg['Subject'] = f"Your Online Exam Result (Mitradnya Publications) ({score}/{total_questions})"
                    student_msg['From'] = TEACHER_NAME
                    student_msg['To'] = student_email
                    
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.starttls()
                    server.login(TEACHER_EMAIL, EMAIL_PASSWORD)
                    server.sendmail(TEACHER_EMAIL, student_email, student_msg.as_string())
                    server.quit()
                    st.info(f"📧 Your Detail Report {student_email} mail on this id.")
                except Exception as e:
                    st.error("ईमेल पाठवण्यात तांत्रिक अडचण आली.")
