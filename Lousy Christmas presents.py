#dmopc '20 contest 2 p2 - lousey christmas presents
n,m = map(int, input().split())
c_inputs = list(map(int, input().split()))
color_first = {}
color_last = {}
final_answer = 0
for i in range(n):
  single_color = c_inputs[i]
  if single_color not in color_first:
    color_first[single_color] = i
  color_last[single_color] = i
for x in range(m):
  a, b = map(int, input().split())
  if a in color_first and b in color_last:
    if color_first[a] < color_last[b]:
      final_distance = (color_last[b] - color_first[a] + 1)
      final_answer = max(final_distance, final_answer)
print(final_answer)
