%global debug_package %{nil}

Summary:        an a11y indicator for wingpanel
Name:           wingpanel-indicator-a11y
Version:        0.1~rev%{rev}
Release:        4%{?dist}
License:        GPLv3
URL:            http://launchpad.net/wingpanel-indicator-a11y

Source0:        %{name}-%{version}.tar.gz
Source1:        %{name}.conf

BuildRequires:  cmake
BuildRequires:  gettext
BuildRequires:  pkgconfig
BuildRequires:  vala >= 0.22.0
BuildRequires:  vala-tools

BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(wingpanel-2.0)


%description
an a11y indicator for wingpanel


%prep
%autosetup


%build
%cmake
%make_build


%install
%make_install


%clean
rm -rf %{buildroot}


%files
%{_libdir}/wingpanel/liba11y.so


%changelog
* Mon May 30 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev3-4
- Update for packaging changes.

* Sun May 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev3-3
- Update for packaging changes.

* Wed May 11 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev3-2
- Update for packaging changes.

* Tue May 10 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev%{rev}-1
- Initial package.

