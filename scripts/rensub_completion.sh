_rensub() 
{
    local cur prev opts
    COMPREPLY=()
    cur="${COMP_WORDS[COMP_CWORD]}"
    prev="${COMP_WORDS[COMP_CWORD-1]}"
    opts="get manage config"
   
    case "${prev}" in
	get)
	    local running=$(rensub manage -l)
	    COMPREPLY=( $(compgen -W "${running}" -- ${cur}) )
            return 0
            ;;
        *)
        ;;
    esac

    COMPREPLY=( $(compgen -W "${opts}" -- ${cur}) )
    return 0
    
}
complete -F _rensub rensub

_getshow() 
{
    local cur prev opts
    COMPREPLY=()
    cur="${COMP_WORDS[COMP_CWORD]}"
    prev="${COMP_WORDS[COMP_CWORD-1]}"
    opts=$(rensub manage -l)

    COMPREPLY=( $(compgen -W "${opts}" -- ${cur}) )
    return 0
    
}
complete -F _getshow getshow
