import bankinterestmodule

amount=float(input("enter Amount to calculate interest :: "))
year=float(input("enter Year to calculate interest :: "))

print("Saving Interest is :: ",bankinterestmodule.savinginterest(amount,year))
print("Resurring Interest is :: ",bankinterestmodule.recurringinterest(amount,year))
print("FD Interest is :: ",bankinterestmodule.fdinterest(amount,year))