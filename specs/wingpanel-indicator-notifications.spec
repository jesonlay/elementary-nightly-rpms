%global debug_package %{nil}

Summary:        a notifications indicator for wingpanel
Name:           wingpanel-indicator-notifications
Version:        0.1~rev%{rev}
Release:        2%{?dist}
License:        GPLv3
URL:            http://launchpad.net/wingpanel-indicator-notifications

Source0:        %{name}-%{version}.tar.gz
Source1:        %{name}.conf

BuildRequires:  cmake
BuildRequires:  gettext
BuildRequires:  pkgconfig
BuildRequires:  vala >= 0.22.0
BuildRequires:  vala-tools

BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libwnck-3.0)
BuildRequires:  pkgconfig(wingpanel-2.0)


%description
a notifications indicator for wingpanel


%prep
%autosetup


%build
%cmake
%make_build


%install
%make_install
%find_lang notifications-indicator


%clean
rm -rf %{buildroot}


%files -f notifications-indicator.lang
%{_libdir}/wingpanel/libnotifications-indicator.so


%changelog
* Sun May 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev92-2
- Update for packaging changes.

* Sat May 28 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev92-1
- Update to latest snapshot.

* Thu May 26 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev91-1
- Update to latest snapshot.

* Wed May 25 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev90-1
- Update to latest snapshot.

* Tue May 24 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev89-1
- Update to latest snapshot.

* Sat May 21 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev86-1
- Update to latest snapshot.

* Thu May 12 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev85-1
- Update to latest snapshot.

* Tue May 10 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev84-2
- Update for packaging changes.

* Tue May 10 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev%{rev}-1
- Initial package.



