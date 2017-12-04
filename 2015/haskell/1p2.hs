import Data.List

pos [] = 0
pos str = pos (init str) + (if last str == '(' then 1 else -1)

solve str = elemIndex (-1) m
    where m = [pos $ take x str | x <- [1..(length str)]]

main = do
    input <- getLine
    putStrLn $ show $ solve input
