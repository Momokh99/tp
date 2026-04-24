local person = { name = "ali", age = 22 }

local greet = function(p)
	return "hi " .. p.name
end

print(greet(person))
