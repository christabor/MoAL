# http://www.westwind.com/reference/os-x/commandline/pipes.html

function divider() {
    echo '\n------------------------------------------------------------------'
}


case "$1" in
    1)
        # http://www.westwind.com/reference/os-x/commandline/navigation.html
        divider
        cd . && ls -la | ag '.py'
    ;;

    2)
        # divider
        pwd | ag 'MOAL'
    ;;

    3)
        case "$2" in
            verbose)
                # Almost quine-like
                divider
                ag 'unix_cmds.sh' | xargs less
                ;;
        esac
    ;;

    4)
        divider
        lsof | more | ag 'ctabor' > lsof-foo.txt
        rm lsof-foo.txt
    ;;

    5)
        tail -2 'unix_cmds.sh'
    ;;

    6)
        divider
        mkdir 'testing-foo' && ls && chown 'ctabor' 'testing-foo' | ag 'testing-foo'
        rm -r 'testing-foo'
    ;;

    7)
        divider
        # Self-similar...
        ps ax | xargs | ag 'foobar'
    ;;

    8)
        divider
        echo 'circular echo -> write output -> less'
        echo 'foo' > 'circular-foo.txt' | less 'circular-foo.txt'
    ;;

    9)
        divider
        echo 'echo -> write append output -> less'
        echo '\nfoo2!' >> 'circular-foo.txt' | less 'circular-foo.txt'
        rm 'circular-foo.txt'
    ;;

    10)
        divider
        echo 'Tee output to file and buffer'
        ls -la | tee 'foo-stuff.txt' | more | ag '.sh'
    ;;

    11)
        divider
        echo 'Man + pipe -> apropos circular'
        man 'sh' | ag 'shell' -0 -wc | xargs apropos | ag 'shell'
esac
