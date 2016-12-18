Summary:        elementary GTK+ Stylesheet
Name:           elementary-themes
Version:        5.0.2+git%{date}.%{rev}
Release:        1%{?dist}
License:        GPLv3
URL:            http://github.com/elementary/stylesheet

Source0:        %{name}-%{version}.tar.gz
Source1:        %{name}.conf

BuildArch:      noarch

Requires:       gtk-murrine-engine


%description
An original Gtk.CSS stylesheet designed specifically for elementary OS
and its desktop environment: Pantheon.


%prep
%autosetup


%build


%install
mkdir -p %{buildroot}/%{_datadir}/themes/elementary

cp -p index.theme %{buildroot}/%{_datadir}/themes/elementary/
cp -pr gtk-2.0 %{buildroot}/%{_datadir}/themes/elementary/
cp -pr gtk-3.0 %{buildroot}/%{_datadir}/themes/elementary/
cp -pr plank %{buildroot}/%{_datadir}/themes/elementary/


%clean
rm -rf %{buildroot}


%files
%doc AUTHORS CONTRIBUTORS HACKING
%license COPYING

%{_datadir}/themes/elementary


%changelog
* Sun Dec 18 2016 Fabio Valentini <decathorpe@gmail.com> - 5.0.2+git161218.174932.727c158a-1
- Update to latest snapshot.

* Sun Oct 16 2016 Fabio Valentini <decathorpe@gmail.com> - 5.0.2+git161015.175037.cb6b93eb-1
- Update to latest snapshot.

* Thu Sep 29 2016 Fabio Valentini <decathorpe@gmail.com> - 5.0.2+git160927.144324.36a46bf9-2
- Spec file cleanups.

* Wed Sep 28 2016 Fabio Valentini <decathorpe@gmail.com> - 5.0.2+git160927.144324.36a46bf9-1
- Update to latest snapshot.

* Sun Sep 25 2016 Fabio Valentini <decathorpe@gmail.com> - 5.0.2+git160925.113001.778259b4-1
- Update to latest snapshot.

* Sat Sep 24 2016 Fabio Valentini <decathorpe@gmail.com> - 5.0.2+git160923.173728.192e7cc8-1
- Update to version 5.0.2.

* Sat Sep 24 2016 Fabio Valentini <decathorpe@gmail.com> - 5.0.1+git160923.173728.192e7cc8-1
- Update to latest snapshot.

* Fri Sep 23 2016 Fabio Valentini <decathorpe@gmail.com> - 5.0.1+git160922.142219.f2f734b3-1
- Update to version 5.0.1.

* Mon Sep 19 2016 Fabio Valentini <decathorpe@gmail.com> - 5.0.1~git160919.163423~877fab28-1
- Update to latest snapshot.

* Mon Sep 19 2016 Fabio Valentini <decathorpe@gmail.com> - 5.0.1~git160919.134452~ad45ee14-1
- Update to latest snapshot.

* Sat Sep 17 2016 Fabio Valentini <decathorpe@gmail.com> - 5.0.1~git160916.205458~8189f96b-1
- Update to latest snapshot.

* Tue Sep 13 2016 Fabio Valentini <decathorpe@gmail.com> - 5.0.1~git160911.211643~3457221a-1
- Update to version 5.0.1.


