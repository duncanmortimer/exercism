parse_single_nucleotide(c::AbstractChar) = (
  c in Set(['A', 'C', 'G', 'T']) 
  ? Dict(c => 1)
  : throw(DomainError(c))
)

function count_nucleotides(strand::AbstractString)
  reduce(
    (d...) -> merge(+, d...),
    map(parse_single_nucleotide, collect(strand));
    init=Dict('A' => 0, 'C' => 0, 'G' => 0, 'T' => 0)
  )
end
