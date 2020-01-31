function distance(s1::AbstractString, s2::AbstractString)
  (
    length(s1) ≠ length(s2) ? throw(ArgumentError("input strings should have the same lengths"))
    : reduce(+, l≠r for (l,r) in zip(s1, s2); init=0)
  )
end
