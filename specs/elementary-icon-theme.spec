Summary:        elementary Icons
Name:           elementary-icon-theme
Version:        4.0.1+git%{date}.%{rev}
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


