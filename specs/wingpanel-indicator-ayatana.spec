%global debug_package %{nil}

Summary:        an ayatana indicator for wingpanel
Name:           wingpanel-indicator-ayatana
Version:        0.1~rev%{rev}
Release:        1%{?dist}
License:        GPLv3
URL:            http://launchpad.net/wingpanel-indicator-ayatana

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
BuildRequires:  pkgconfig(indicator3-0.4)
BuildRequires:  pkgconfig(wingpanel-2.0)


%description
an ayatana indicator for wingpanel


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
# %{_libdir}/wingpanel/libayatana.so


%changelog
* Tue May 10 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev%{rev}-1
- Initial package.

