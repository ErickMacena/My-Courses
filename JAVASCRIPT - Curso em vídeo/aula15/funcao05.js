/*function recursive_fat(n, fat = 1)
{
    if(n == 1)
    {
        return fat
    }
    else
    {
        return recursive_fat(n - 1, fat * n)
    }
}

console.log(recursive_fat(30))*/

function recursive_fat2(n)
{
    if(n == 1)
    {
        return 1
    }
    else
    {
        return n * recursive_fat2(n - 1)
    }
}

console.log(recursive_fat2(5))