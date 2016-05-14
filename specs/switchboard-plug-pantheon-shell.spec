%global debug_package %{nil}

Summary:        Configure various aspects of the Pantheon desktop environment
Name:           switchboard-plug-pantheon-shell
Version:        0.2.2.1~rev%{rev}
Release:        1%{?dist}
License:        GPLv3
URL:            http://launchpad.net/switchboard-plug-pantheon-shell

Source0:        %{name}-%{version}.tar.gz
Source1:        %{name}.conf

BuildRequires:  cmake
BuildRequires:  gettext
BuildRequires:  pkgconfig
BuildRequires:  vala >= 0.22.0
BuildRequires:  vala-tools

BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  pkgconfig(gnome-desktop-3.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(plank)
BuildRequires:  pkgconfig(switchboard-2.0)

Requires:       contractor


%description
The desktop plug is a section in Switchboard, the elementary System Settings app, where users can configure the wallpaper, dock, and hotcorners. In the future the desktop plug might also handle other desktop settings such as the panel, app launcher, and window manager.

Designed for elementary OS.


%prep
%autosetup


%build
%cmake
%make_build


%install
%make_install
%find_lang pantheon-desktop-plug


%clean
rm -rf %{buildroot}


%files -f pantheon-desktop-plug.lang
%{_bindir}/set-wallpaper

%{_libdir}/switchboard/personal/pantheon-desktop/

%{_datadir}/contractor/set-wallpaper.contract


%changelog
* Tue May 10 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev%{rev}-1
- Initial package.

