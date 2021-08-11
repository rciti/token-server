randString <- function(characters = 0, numbers = 0, symbols = 0, lowerCase = 0, upperCase = 0) {
    ASCII <- NULL
    if (symbols > 0) ASCII <- c(ASCII, sample(c(33:47, 58:34, 91:96, 123:126), symbols))
    if (numbers > 0) ASCII <- c(ASCII, sample(48:57, numbers))
    if (upperCase > 0) ASCII <- c(ASCII, sample(65:90, upperCase))
    if (lowerCase > 0) ASCII <- c(ASCII, sample(97:122, lowerCase))
    if (characters > 0) ASCII <- c(ASCII, sample(c(65:90, 97:122), characters))

    return(rawToChar(as.raw(sample(ASCII, length(ASCII)))))
}

max_length <- 8

tokens <- sapply(seq_len(1000), function(x) {
    n_chars <- sample(4:7, 1)
    n_nums <- max_length - n_chars
    randString(characters = n_chars, numbers = n_nums)
})

write.table(tokens, "tokens.csv",
    row.names = FALSE,
    col.names = FALSE,
    quote = FALSE
)
