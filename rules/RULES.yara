rule YR_TEST {
    meta:
        description = "Test if the script works by checking if res contains space"
        author = "@mossdinger"

    strings:
        $html1 = " "

    condition:
        $html1
}