Name:           elementary-theme
Summary:        elementary GTK+ Stylesheet
Version:        5.0.4+git%{date}.%{commit}
Release:        1%{?dist}
License:        GPLv3
URL:            https://github.com/elementary/stylesheet

Source0:        %{name}-%{version}.tar.gz
Source1:        %{name}.conf

BuildArch:      noarch


%description
An original Gtk.CSS stylesheet designed specifically for elementary OS
and its desktop environment: Pantheon.


%package        gtk2
Summary:        elementary GTK+ Stylesheet for GTK+2

Requires:       %{name} = %{version}-%{release}
Requires:       gtk-murrine-engine

Supplements:    (%{name} and gtk2)

%description    gtk2
An original Gtk.CSS stylesheet designed specifically for elementary OS
and its desktop environment: Pantheon.

This package contains the GTK+2 theme.


%package        gtk3
Summary:        elementary GTK+ Stylesheet for GTK+3

Requires:       %{name} = %{version}-%{release}

Supplements:    (%{name} and gtk3)

%description    gtk3
An original Gtk.CSS stylesheet designed specifically for elementary OS
and its desktop environment: Pantheon.

This package contains the GTK+3 theme.


%package        plank
Summary:        elementary GTK+ Stylesheet for plank

Requires:       %{name} = %{version}-%{release}

Supplements:    (%{name} and plank)

%description    plank
An original Gtk.CSS stylesheet designed specifically for elementary OS
and its desktop environment: Pantheon.

This package contains the plank theme.


%prep
%autosetup


%build
# Nothing to do


%install
mkdir -p %{buildroot}/%{_datadir}/themes/elementary

cp -p index.theme %{buildroot}/%{_datadir}/themes/elementary/
cp -pr gtk-2.0 %{buildroot}/%{_datadir}/themes/elementary/
cp -pr gtk-3.0 %{buildroot}/%{_datadir}/themes/elementary/
cp -pr plank %{buildroot}/%{_datadir}/themes/elementary/


%files
%doc AUTHORS CONTRIBUTORS README.md
%license COPYING

%dir %{_datadir}/themes/elementary
%{_datadir}/themes/elementary/index.theme

%files          gtk2
%{_datadir}/themes/elementary/gtk-2.0/

%files          gtk3
%{_datadir}/themes/elementary/gtk-3.0/

%files          plank
%{_datadir}/themes/elementary/plank/


%changelog
* Mon May 01 2017 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git170501.094928.bf0893a0-1
- Update to latest snapshot.

* Mon May 01 2017 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git170430.094741.471ffaeb-2
- Adapt to upstream file changes.

* Sun Apr 30 2017 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git170430.094741.471ffaeb-1
- Update to latest snapshot.

* Sat Apr 29 2017 Fabio Valentini <decathorpe@gmail.com> - 5.0.4+git170212.162057.5f600c6b-1
- Update to version 5.0.4.

* Wed Feb 08 2017 Fabio Valentini <decathorpe@gmail.com> - 5.0.3+git170128.184610.01d0411e-1
- Update to latest snapshot.

* Wed Feb 08 2017 Fabio Valentini <decathorpe@gmail.com> - 5.0.3+git170128.184610.01d0411e-2
- Sync spec with fedora package.

* Fri Jan 20 2017 Fabio Valentini <decathorpe@gmail.com> - 5.0.3+git170115.161326.548fac7c-1
- Update to version 5.0.3.

* Wed Jan 18 2017 Fabio Valentini <decathorpe@gmail.com> - 5.0.2+git170115.161326.548fac7c-1
- Update to latest snapshot.

* Wed Jan 18 2017 Fabio Valentini <decathorpe@gmail.com> - 5.0.2+git161218.174932.727c158a-1
- Update to version 5.0.2.

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


