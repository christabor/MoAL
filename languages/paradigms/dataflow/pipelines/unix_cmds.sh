
function divider() {
    echo '\n------------------------------------------------------------------'
}

# ------------------------------------------------------------------------------
#              http://www.westwind.com/reference/os-x/commandline/
# ------------------------------------------------------------------------------

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

    12)
        divider
        echo 'Find types + pipes'
        find . -type f -print0 | xargs -0 ag -il 'shell' | xargs wc

    13)
        divider
        echo 'Locate + weird circular find'
        locate 'pipeline' | ag '.py' | xargs find . | ag '.py' | wc

    14)
        divider
        echo 'With extreme prejudice'
        lsof -b | ag 'microsoft' | xargs pkill

    15)
        divider
        echo 'Find default ethernet'
        ifconfig -a | ag 'en0'

    16)
        divider
        echo 'homesweethome'
        sw_vers | ag 'Mac'


# ------------------------------------------------------------------------------
#              http://www.tldp.org/LDP/abs/html/sedawk.html
# ------------------------------------------------------------------------------

    17)
        divider
        echo 'sed + pipes 1 - print'
        ls -la ~/ | sed -n '/@/p'

    18)
        divider
        echo 'sed substitution and output'
        ps ax | ag 'ctabor' > procs.txt && less procs.txt | sed -n 's/ctabor/CTABULOUS/p' > procs2.txt

    19)
        divider
        echo 'Prettify list'
        sw_vers | awk '{print $1 " ==> " $2}' | sed -n 's/://p' > preeetty.txt

esac
