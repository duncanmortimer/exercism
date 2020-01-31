complement(c::AbstractChar) = (
  c == 'G' ? 'C'
  : c == 'C' ? 'G'
  : c == 'T' ? 'A'
  : c == 'A' ? 'U'
  : throw(ErrorException("Input should only contain A, C, G, or T"))
)

function to_rna(dna::AbstractString)
  map(complement, dna)
end

