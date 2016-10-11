path_prepend() {
    local result=$1

    case ":${result:=$2}:" in
        *:$2:*) ;;
        *) result="$2:$result" ;;
    esac

    echo "$result"
}

export PATH=$(path_prepend "$PATH" "/opt/nvidia-common/bin")
export PKG_CONFIG_PATH=$(path_prepend "$PKG_CONFIG_PATH" "/opt/nvidia-common/lib64/pkgconfig")
export MANPATH=$(path_prepend "$(manpath 2>/dev/null)" "/opt/nvidia-common/share/man")

unset path_prepend
