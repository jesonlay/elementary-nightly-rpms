Summary:        Lightweight and stylish app launcher
Name:           slingshot-launcher
Version:        0.9.0~rev%{rev}
Release:        0%{?dist}
License:        GPLv3
URL:            http://launchpad.net/slingshot

Source0:        %{name}-%{version}.tar.gz
Source1:        %{name}.conf

BuildRequires:  cmake
BuildRequires:  gettext
BuildRequires:  pkgconfig
BuildRequires:  vala >= 0.26.2
BuildRequires:  vala-tools

BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.12.0
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libgnome-menu-3.0)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(plank) >= 0.10.9
BuildRequires:  pkgconfig(switchboard-2.0)
BuildRequires:  pkgconfig(wingpanel-2.0)
BuildRequires:  pkgconfig(zeitgeist-2.0)


%description
The lightweight and stylish app launcher from elementary.

Designed for elementary OS.


%prep
%autosetup


%build
%cmake -DUSE_UNITY:BOOL=OFF -DUSE_ZEITGEIST:BOOL=ON
%make_build


%install
%make_install
%find_lang slingshot


%clean
rm -rf %{buildroot}


%files
%doc AUTHORS
%license COPYING


%changelog

