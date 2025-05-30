footbal_starts = ["Messi", "Ronaldo", "Maradona", "Best", "Puskas"]

index = footbal_starts.index("Ronaldo")
footbal_starts.remove("Ronaldo")
footbal_starts.insert(index, "Cristiano Ronaldo")
print(footbal_starts)