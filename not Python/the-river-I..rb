# puzzle // https://www.codingame.com/ide/puzzle/the-river-i-

r1 = gets.to_i
r2 = gets.to_i

while r1 != r2 do
  if r1 < r2
    r1+= r1.digits.sum
  else
    r2+= r2.digits.sum
  end  
end

puts r1
