%global _nvidia_prefix      /opt/nvidia-common
%global _nvidia_bindir      %{_nvidia_prefix}/bin
%global _nvidia_includedir  %{_nvidia_prefix}/include
%global _nvidia_libdir      %{_nvidia_prefix}/lib64
%global _nvidia_lib32dir    %{_nvidia_prefix}/lib
%global _nvidia_datadir     %{_nvidia_prefix}/share
%global _nvidia_docdir      %{_nvidia_prefix}/share/doc
%global _nvidia_mandir      %{_nvidia_prefix}/share/man

Name:           nvidia-common
Version:        1.0.0
Release:        6%{?dist}
Summary:        System integration tools for NVIDIA proprietary software

License:        MIT
Source0:        nvidia-common-x86_64.conf
Source1:        nvidia-common.sh
BuildArch:      noarch


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
install -d %{buildroot}%{_nvidia_lib32dir}/
install -d %{buildroot}%{_nvidia_docdir}/
install -d %{buildroot}%{_nvidia_mandir}/
install -d %{buildroot}%{_nvidia_mandir}/man{1,n,l,8,3,0,2,5,4,9,6,7}/

sed -e 's;@NVIDIA_BINDIR@;%{_nvidia_bindir};' \
    -e 's;@NVIDIA_LIBDIR@;%{_nvidia_libdir};' \
    -e 's;@NVIDIA_MANDIR@;%{_nvidia_mandir};' \
    -i %{SOURCE0} %{SOURCE1}

install -p -m 0644 %{SOURCE0} %{buildroot}%{_sysconfdir}/ld.so.conf.d/
install -p -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/profile.d/

cat >> %{buildroot}/usr/lib/rpm/macros.d/macros.%{name} <<EOF
%%_nvidia_prefix        %_nvidia_prefix
%%_nvidia_bindir        %_nvidia_bindir
%%_nvidia_includedir    %_nvidia_includedir
%%_nvidia_libdir        %_nvidia_libdir
%%_nvidia_lib32dir      %_nvidia_lib32dir
%%_nvidia_datadir       %_nvidia_datadir
%%_nvidia_docdir        %_nvidia_docdir
%%_nvidia_mandir        %_nvidia_mandir
EOF


%files
%dir %{_nvidia_prefix}/
%dir %{_nvidia_bindir}/
%dir %{_nvidia_includedir}/
%dir %{_nvidia_libdir}/
%dir %{_nvidia_libdir}/pkgconfig/
%dir %{_nvidia_lib32dir}/
%dir %{_nvidia_datadir}/
%dir %{_nvidia_docdir}/
%dir %{_nvidia_mandir}/
%dir %{_nvidia_mandir}/man*/
%config %{_sysconfdir}/ld.so.conf.d/*
%config %{_sysconfdir}/profile.d/*
/usr/lib/rpm/macros.d/*


%changelog
* Tue Oct 11 2016 Jajauma's Packages <jajauma@yandex.ru> - 1.0.0-6
- Fix manpath redirection error

* Thu Oct 06 2016 Jajauma's Packages <jajauma@yandex.ru> - 1.0.0-5
- Public release
