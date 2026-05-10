local temp = 24

if temp < 10 then
	print("it's cold")
elseif temp > 30 then
	print("its hot")
else
	print("normal")
end

for i = 0, 10, 2 do
	print("this is " .. i)
end

while temp < 88 do
	print("y \n")
	temp = 1 + temp
end
