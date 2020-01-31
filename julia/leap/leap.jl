can_divide(n::Int; by::Int) = rem(n, by) == 0

function is_leap_year(year::Int)
   (
       can_divide(year, by=400) ? true
       : can_divide(year, by=100) ? false
       : can_divide(year, by=4)
   )
end