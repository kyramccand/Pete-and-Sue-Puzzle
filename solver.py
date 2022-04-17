
'''
Suppose we have two numbers 𝑋 and 𝑌, such that 1<𝑋<𝑌<100, and 
𝑋+𝑌≤100. Sue is given 𝑆=𝑋+𝑌 and Pete is given 𝑃=𝑋𝑌.

They then have the following conversation:

     Pete: 'I do not know the two numbers.'

     Sue: 'I knew you didn’t know. I don’t know either.'

     Pete: 'Now I know the two numbers.'

     Sue: 'Now I know the two numbers.'
'''
import math

def is_prime(num):
  prime = True
  if num % 2 == 0 and num != 2:
    prime = False
  else:
    floored_square_root = int(math.sqrt(num))
    for possible_fact in range(floored_square_root):
      if possible_fact + 1 >= 3:
        if num % (possible_fact + 1) == 0:
          prime = False
  return prime

prime_list = []
for num in range(100):
  if is_prime(num + 1) == True:
    prime_list.append(num + 1)

#print(prime_list)
          
    
        

pair_list = []
num_list = []

for num in range(100):
  if num >= 2 and num <= 99:
    num_list.append(num)


for num1 in num_list:
  for num2 in num_list:
    if num1 != num2:
      possible_pair = [num1, num2]
      possible_pair.sort()
      if possible_pair not in pair_list:
        if num1 + num2 <= 100:
          pair_list.append(possible_pair)


print(len(pair_list))
petes_pair_list = list(pair_list)
#print(f'same_list? = {pair_list is petes_pair_list}')


prime_pairs = []

for prime1 in prime_list:
  for prime2 in prime_list:
    if prime1 != prime2:
      prime_pair = [prime1, prime2]
      prime_pair.sort()
      if prime_pair not in prime_pairs:
        prime_pairs.append(prime_pair)

print(f'length of prime_pairs = {len(prime_pairs)}')

if False:
  print(f'before removing prime pairs, length of petes_pair_list = {len(petes_pair_list)}')
  for prime_pair in prime_pairs:
    if prime_pair in petes_pair_list:
      petes_pair_list.remove(prime_pair)
  print(f'after removing prime pairs, length of petes_pair_list = {len(petes_pair_list)}')

by_product = {}
for x, y in petes_pair_list:
  product = x * y
  if product not in by_product:
    by_product[product] = []
  by_product[product].append([x, y])

for key,value in by_product.items():
  if len(value) == 1:
    petes_pair_list.remove(value[0])
    print(f'removing {value[0]}')
  print(f'for product = {key}, x, y = {value}')

print(f'after removing singleton products, length of petes_pair_list = {len(petes_pair_list)}')

  

by_sum = {}
for x, y in pair_list:
  sum = x + y
  if sum not in by_sum:
    by_sum[sum] = []
  by_sum[sum].append([x, y])

for key, value in sorted(by_sum.items()):
  print(f'for sum {key}, there are {value}')

print(f'len(by_sum) is {len(by_sum)}')
#print(by_sum)
      
must_del_list = []

for sum in sorted(by_sum.keys()):
  for x, y in by_sum[sum]:
    assert x < y
    if [x, y] not in petes_pair_list:
      must_del_list.append(sum)
      print(f'i am deleting sum {sum} because {[x, y]} sum to that')
      break

print(f'length of must_del_list = {len(must_del_list)}')

del_count = 0

for del_sum in must_del_list:
  del by_sum[del_sum]
  del_count += 1

print(f'deleted {del_count} pairs')

print(f'number of sums left: {len(by_sum)}')

print(by_sum.keys())

if False:
  petes_set = set()
  
  for x, y in petes_pair_list:
    petes_set.add((x, y))

  print(f'the length of petes_set: {len(petes_set)}')

sues_set = set()

for l in by_sum.values():
  for x, y in l:
    sues_set.add((x, y))

print(f'the length of sues_set: {len(sues_set)}')\

if False:
  both_set = sues_set.intersection(petes_set)
  
  print(f'length of intersected set: {len(both_set)}')

for key,value in sorted(by_sum.items()):
  print(f'sum of {key} only these possible values: {value}')

#print(sorted(both_set))


by_product_two = {}

for x, y in sues_set:
  product = x * y
  if product not in by_product_two:
    by_product_two[product] = []
  by_product_two[product].append((x, y))

for key, value in sorted(by_product_two.items()):
  print(f'for product = {key}, all possible pairs are: {value}')

remaining_set = set()

for key, value in sorted(by_product_two.items()):
  if len(value) == 1:
    remaining_set.add(value[0])

print(f'{remaining_set} \n length of remaining_set = {len(remaining_set)}')

by_sum_two = {}

for x, y in remaining_set:
  sum = x + y
  if sum not in by_sum_two:
    by_sum_two[sum] = []
  by_sum_two[sum].append((x, y))

for key, value in sorted(by_sum_two.items()):
  print(f'for sum = {key}, all possible pars are: {value}')
  
