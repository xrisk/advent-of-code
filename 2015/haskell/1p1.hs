count str c = length $ filter (== c) str
solve str = count str '(' - count str ')' 

main = do
    l <- getLine
    putStrLn $ show $ solve l
