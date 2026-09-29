import chromadb

client = chromadb.PersistentClient(path="chroma_db")
col = client.get_collection("docs")

# (question, expected source filename without .txt)
# Assuming the images are named 21 through 31 in the order they were uploaded
TESTS = [
    
    ("What is the ending balance for the Howard Relationship Checking account ending in 4101?", "43"),
    ("What is the primary branch for the Howard Bank account?", "43"),
    ("What was the amount of the Signature POS Debit at MD Baltimore Giant Food on 09/04/2018?", "43"),

    
    ("What is the account number for the Demo BusinessSelect Checking account?", "42"),
    ("What is the ending balance of the Demo Business Select High Yield Savings account?", "42"),
    ("How many checks were paid from the Demo BusinessSelect Checking account?", "42"),

    # --- Image 3 (Expected: 23) ---
    ("What is the total balance on the Bank of America combined statement for Sam Bobley?", "41"),
    ("What is the ending balance for the Adv Plus Banking account?", "41"),
    ("What is the statement period for the Bank of America statement?", "41"),

    # --- Image 4 (Expected: 24) ---
    ("What is the closing balance for John Smith's BNI personal current account?", "39"),
    ("What is the card number associated with the BNI account?", "39"),
    ("What was the total debit amount for the BNI statement?", "39"),

    # --- Image 5 (Expected: 25) ---
    ("What is the closing balance on April 18, 2010 for Mary Jane Smith?", "22"),
    ("What is the account number for the Metro Bank account?", "22"),
    ("What was the amount of the ATM withdrawal on April 10?", "22"),

    

    # --- Image 7 (Expected: 27) ---
    ("What is the account number for Miss Illumelany Moshayi's Capitec Bank savings account?", "20"),
    ("What is the balance after the Cash Withdrawal Fee on 31/08/2018?", "20"),
    ("What is the VAT Registration Number for Capitec Bank?", "20"),

    # --- Image 8 (Expected: 28) ---
    #("What is the account name for account number 30000100003115?", "33"),
    #("What was the amount of the transaction to PGDR/ONE97 COMMUNICATIONS on 16/10/15?", "33"),
    #("What is the debit amount for the transaction on 17/10/15?", "33"),

    # --- Image 9 (Expected: 29) ---
    #("What is the IFSC code for the Punjab National Bank MUZAFFARPUR branch?", "28"),
    #("What is the balance after the UPI transaction on 17/12/2019?", "28"),
    #("What is the customer name on the Punjab National Bank statement?", "28"),

    # --- Image 10 (Expected: 30) ---
    #("What is the closing balance for Adama Amad's account at Big Bank of Bucks?", "24"),
    #("What was the amount of the Direct Deposit Payroll on 15th June?", "24"),
    #("What is the branch number for the Big Bank of Bucks account?", "24"),

    # --- Image 11 (Expected: 31) ---
    ("What are the ticket prices for the Forever Plaid musical?", "plaid_c150"),
    ("What are the showtimes for Forever Plaid on Fridays and Saturdays?", "plaid_c150"),
    ("What is the phone number to buy tickets for Forever Plaid?", "plaid_c150"),
]

hits = 0
for q, expected in TESTS:
    res = col.query(query_texts=[q], n_results=3)
    sources = [m["source"] for m in res["metadatas"][0]]
    ok = expected in sources
    hits += ok
    print("HIT " if ok else "MISS", q, "->", sources)

print(f"\nHit rate @3: {hits}/{len(TESTS)} = {hits / len(TESTS):.0%}")