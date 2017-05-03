Summary:        elementary Icons
Name:           elementary-icon-theme
Version:        4.0.3+git%{date}.%{commit}
Release:        1%{?dist}
License:        GPLv3+
URL:            https://launchpad.net/elementaryicons

Source0:        %{name}-%{version}.tar.gz
Source1:        %{name}.conf

BuildArch:      noarch


%description
This is an icon theme designed to be smooth, sexy, clear, and efficient.


%prep
%autosetup


%build
# Nothing to do.


%install
mkdir -p %{buildroot}/%{_datadir}/icons/elementary
cp -apR * %{buildroot}/%{_datadir}/icons/elementary

rm %{buildroot}/%{_datadir}/icons/elementary/AUTHORS
rm %{buildroot}/%{_datadir}/icons/elementary/CONTRIBUTORS
rm %{buildroot}/%{_datadir}/icons/elementary/COPYING
rm %{buildroot}/%{_datadir}/icons/elementary/pre-commit
rm %{buildroot}/%{_datadir}/icons/elementary/README.md

touch %{buildroot}/%{_datadir}/icons/elementary/icon-theme.cache


%post
/bin/touch --no-create %{_datadir}/icons/elementary &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/elementary &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/elementary &>/dev/null || :
fi

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/elementary &>/dev/null || :


%files
%doc AUTHORS CONTRIBUTORS
%license COPYING

%{_datadir}/icons/elementary
%ghost %{_datadir}/icons/elementary/icon-theme.cache


%changelog
* Wed May 03 2017 Fabio Valentini <decathorpe@gmail.com> - 4.0.3+git170503.115336.5a241a59-1
- Update to latest snapshot.

* Tue May 02 2017 Fabio Valentini <decathorpe@gmail.com> - 4.0.3+git170502.134849.6e3679ff-1
- Update to latest snapshot.

* Tue May 02 2017 Fabio Valentini <decathorpe@gmail.com> - 4.0.3+git170501.172536.2b901ccd-1
- Update to latest snapshot.

* Sun Apr 30 2017 Fabio Valentini <decathorpe@gmail.com> - 4.0.3+git170425.165220.c27c0112-1
- Update to latest snapshot.

* Mon Mar 20 2017 Fabio Valentini <decathorpe@gmail.com> - 4.0.3+git170320.103314.77291de6-1
- Update to latest snapshot.

* Mon Mar 20 2017 Fabio Valentini <decathorpe@gmail.com> - 4.0.3+git170227.130409.6c5effa8-1
- Update to version 4.0.3.

* Sat Mar 04 2017 Fabio Valentini <decathorpe@gmail.com> - 4.0.2+git170227.130409.6c5effa8-1
- Update to latest snapshot.

* Wed Feb 08 2017 Fabio Valentini <decathorpe@gmail.com> - 4.0.2+git170202.220804.fdbcf47b-1
- Update to latest snapshot.

* Wed Feb 08 2017 Fabio Valentini <decathorpe@gmail.com> - 4.0.2+git170116.125315.83c6f271-2
- Sync spec with fedora package.

* Thu Jan 19 2017 Fabio Valentini <decathorpe@gmail.com> - 4.0.2+git170116.125315.83c6f271-1
- Update to version 4.0.2.

* Wed Jan 18 2017 Fabio Valentini <decathorpe@gmail.com> - 4.0.1.1+git170116.125315.83c6f271-1
- Update to latest snapshot.

* Wed Jan 18 2017 Fabio Valentini <decathorpe@gmail.com> - 4.0.1.1+git161221.100345.7e9575f6-1
- Update to version 4.0.1.1.

* Wed Dec 21 2016 Fabio Valentini <decathorpe@gmail.com> - 4.0.1.1+git161221.100345.7e9575f6-1
- Update to latest snapshot.

* Sun Dec 18 2016 Fabio Valentini <decathorpe@gmail.com> - 4.0.1.1+git161218.084045.bacf93dc-1
- Update to latest snapshot.

* Sat Dec 17 2016 Fabio Valentini <decathorpe@gmail.com> - 4.0.1.1+git161216.191803.a6743da8-1
- Update to latest snapshot.

* Thu Dec 15 2016 Fabio Valentini <decathorpe@gmail.com> - 4.0.1.1+git161215.100355.c2e60822-1
- Update to latest snapshot.

* Wed Dec 14 2016 Fabio Valentini <decathorpe@gmail.com> - 4.0.1.1+git161214.122150.7d0c52c6-1
- Update to latest snapshot.

* Thu Dec 01 2016 Fabio Valentini <decathorpe@gmail.com> - 4.0.1.1+git161201.145742.c646545c-1
- Update to latest snapshot.

* Thu Dec 01 2016 Fabio Valentini <decathorpe@gmail.com> - 4.0.1.1+git161130.143018.f751b03b-1
- Update to latest snapshot.

* Sat Nov 19 2016 Fabio Valentini <decathorpe@gmail.com> - 4.0.1.1+git161025.124600.181998c1-1
- Update to version 4.0.1.1.

* Tue Oct 25 2016 Fabio Valentini <decathorpe@gmail.com> - 4.0.1+git161025.124600.181998c1-1
- Update to latest snapshot.

* Tue Oct 18 2016 Fabio Valentini <decathorpe@gmail.com> - 4.0.1+git161018.124244.8e52e9b7-1
- Update to latest snapshot.

* Wed Oct 12 2016 Fabio Valentini <decathorpe@gmail.com> - 4.0.1+git161011.215041.c95cfe62-1
- Update to latest snapshot.

* Tue Oct 11 2016 Fabio Valentini <decathorpe@gmail.com> - 4.0.1+git161011.103850.0e1a7d60-1
- Update to latest snapshot.

* Thu Sep 29 2016 Fabio Valentini <decathorpe@gmail.com> - 4.0.1+git160920.130844.24a317fc-1
- Update to version 4.0.1.

* Thu Sep 29 2016 Fabio Valentini <decathorpe@gmail.com> - 4.0.1~git160920.130844~24a317fc-2
- Spec file cleanups.

* Wed Sep 21 2016 Fabio Valentini <decathorpe@gmail.com> - 4.0.1~git160920.130844~24a317fc-1
- Update to latest snapshot.

* Tue Sep 20 2016 Fabio Valentini <decathorpe@gmail.com> - 4.0.1~git160919.212218~47f10bd5-1
- Update to latest snapshot.

* Tue Sep 13 2016 Fabio Valentini <decathorpe@gmail.com> - 4.0.1~git160911.193229~1d70ea96-1
- Update to version 4.0.1.


