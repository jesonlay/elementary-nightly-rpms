%global debug_package %{nil}

Summary:        Mouse and Touchpad configuration management
Name:           switchboard-plug-mouse-touchpad
Version:        0.1.1~rev%{rev}
Release:        3%{?dist}
License:        GPLv3
URL:            http://launchpad.net/switchboard-plug-mouse-touchpad

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
BuildRequires:  pkgconfig(switchboard-2.0)


%description
This is a swtichboard plug for elementary os.


%prep
%autosetup


%build
%cmake
%make_build


%install
%make_install
%find_lang pantheon-mouse-touchpad


%clean
rm -rf %{buildroot}


%files -f pantheon-mouse-touchpad.lang
%{_libdir}/switchboard/hardware/pantheon-mouse-touchpad/


%changelog
* Sun May 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev56-3
- Update for packaging changes.

* Fri May 13 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev56-2
- Update for packaging changes.

* Tue May 10 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev%{rev}-1
- Initial package.

