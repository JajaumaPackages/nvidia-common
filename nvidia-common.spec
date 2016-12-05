%global _nvidia_prefix      /opt/nvidia-common
%global _nvidia_bindir      %{_nvidia_prefix}/bin
%global _nvidia_includedir  %{_nvidia_prefix}/include
%global _nvidia_libdir      %{_nvidia_prefix}/%{_lib}
%global _nvidia_datadir     %{_nvidia_prefix}/share
%global _nvidia_docdir      %{_nvidia_prefix}/share/doc
%global _nvidia_mandir      %{_nvidia_prefix}/share/man

Name:           nvidia-common
Version:        1.0.0
Release:        7%{?dist}
Summary:        System integration tools for NVIDIA proprietary software

Source0:        macros.nvidia-common
License:        MIT
ExclusiveArch:  %{?ix86} x86_64


%description
This package provides means to expose NVIDIA propritary tools and libraries to
the user.


%prep


%build


%install
rm -rf %{buildroot}

install -d %{buildroot}%{_sysconfdir}/ld.so.conf.d/
install -d %{buildroot}%{_sysconfdir}/profile.d/
install -d %{buildroot}/usr/lib/rpm/macros.d/
install -d %{buildroot}%{_nvidia_bindir}/
install -d %{buildroot}%{_nvidia_includedir}/
install -d %{buildroot}%{_nvidia_libdir}/
install -d %{buildroot}%{_nvidia_libdir}/pkgconfig/
install -d %{buildroot}%{_nvidia_docdir}/
install -d %{buildroot}%{_nvidia_mandir}/
install -d %{buildroot}%{_nvidia_mandir}/man{1,n,l,8,3,0,2,5,4,9,6,7}/

install -p -m 644 %{SOURCE0} %{buildroot}/usr/lib/rpm/macros.d/macros.nvidia-common

echo "%{_nvidia_libdir}" > %{buildroot}/etc/ld.so.conf.d/nvidia-common-%{_arch}.conf
cat >> %{buildroot}%{_sysconfdir}/profile.d/nvidia-common-%{_arch}.sh <<'EOF'
path_prepend() {
    local result=$1

    case ":${result:=$2}:" in
        *:$2:*) ;;
        *) result="$2:$result" ;;
    esac

    echo "$result"
}

export PATH=$(path_prepend "$PATH" "/opt/nvidia-common/bin")
export PKG_CONFIG_PATH=$(path_prepend "$PKG_CONFIG_PATH" "%{_nvidia_libdir}/pkgconfig")
export MANPATH=$(path_prepend "$(manpath 2>/dev/null)" "/opt/nvidia-common/share/man")

unset path_prepend
EOF


%files
%dir %{_nvidia_prefix}/
%dir %{_nvidia_bindir}/
%dir %{_nvidia_includedir}/
%dir %{_nvidia_libdir}/
%dir %{_nvidia_libdir}/pkgconfig/
%dir %{_nvidia_datadir}/
%dir %{_nvidia_docdir}/
%dir %{_nvidia_mandir}/
%dir %{_nvidia_mandir}/man*/
%config %{_sysconfdir}/ld.so.conf.d/nvidia-common-%{_arch}.conf
%config %{_sysconfdir}/profile.d/nvidia-common-%{_arch}.sh
/usr/lib/rpm/macros.d/macros.nvidia-common


%changelog
* Mon Dec 05 2016 Jajauma's Packages <jajauma@yandex.ru> - 1.0.0-7
- Rebuilt for altarch
- Drop _nvidia_lib32dir macro

* Tue Oct 11 2016 Jajauma's Packages <jajauma@yandex.ru> - 1.0.0-6
- Fix manpath redirection error

* Thu Oct 06 2016 Jajauma's Packages <jajauma@yandex.ru> - 1.0.0-5
- Public release
