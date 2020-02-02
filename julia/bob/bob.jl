is_question(s::AbstractString) = rstrip(s)[end] == '?'
has_no_content(s::AbstractString) = strip(s) == ""
is_yelling(s::AbstractString) = uppercase(s) == s && occursin(r"[a-zA-Z]", s)

function bob(stimulus::AbstractString)
  has_no_content(stimulus) && return "Fine. Be that way!"
  is_question(stimulus) && is_yelling(stimulus) && return "Calm down, I know what I'm doing!"
  is_question(stimulus) && return "Sure."
  is_yelling(stimulus) && return "Whoa, chill out!"
  "Whatever."
end
