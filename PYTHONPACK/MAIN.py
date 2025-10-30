from Two_D.circle import area as c_area,perimeter as c_perimeter
from Two_D.rectangle import area as r_area,perimeter as r_perimeter
from Two_D.Three_D.cuboid import area as cu_area,perimeter as  cu_perimeter
from Two_D.Three_D.sphere import area as s_area,perimeter as s_perimeter






print("circle area:",c_area(4))
print("circle perimeter:",c_perimeter(4))


print("rectangle area:",r_area(3,4))
print("rectangle perimeter:",r_perimeter(3,4))


print("cuboid area:",cu_area(3,4,5))
print("cuboid perimeter:",cu_perimeter(3,4,5))


print("area of sphere:",s_area(3))
print("perimeter of sphere:",s_perimeter(3))
