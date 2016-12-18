Summary:        elementary Icons
Name:           elementary-icon-theme
Version:        4.0.1.1+git%{date}.%{rev}
Release:        1%{?dist}
License:        GPLv3
URL:            http://launchpad.net/elementaryicons

Source0:        %{name}-%{version}.tar.gz
Source1:        %{name}.conf

BuildArch:      noarch


%description
An original set of vector icons designed specifically for elementary OS
and its desktop environment: Pantheon.


%prep
%autosetup


%build


%install
mkdir -p %{buildroot}/%{_datadir}/icons/elementary

cp -pr * %{buildroot}/%{_datadir}/icons/elementary/

rm %{buildroot}/%{_datadir}/icons/elementary/AUTHORS
rm %{buildroot}/%{_datadir}/icons/elementary/CONTRIBUTORS
rm %{buildroot}/%{_datadir}/icons/elementary/COPYING
rm %{buildroot}/%{_datadir}/icons/elementary/README.md
rm %{buildroot}/%{_datadir}/icons/elementary/pre-commit


%clean
rm -rf %{buildroot}


%files
%doc AUTHORS CONTRIBUTORS
%license COPYING

%{_datadir}/icons/elementary


%changelog
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


