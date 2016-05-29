%global debug_package %{nil}

Summary:        Application configuration management
Name:           switchboard-plug-applications
Version:        0.1.0.2~rev%{rev}
Release:        2%{?dist}
License:        LGPLv3
URL:            http://launchpad.net/switchboard-plug-applications

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
The applications plug is a section in the Switchboard (System Settings) that allows the user to manage application settings.

Built for elementary OS.


%prep
%autosetup


%build
%cmake
%make_build


%install
%make_install
%find_lang applications-plug


%clean
rm -rf %{buildroot}


%files -f applications-plug.lang
%{_libdir}/switchboard/personal/pantheon-applications-plug/


%changelog
* Sun May 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev137-2
- Update for packaging changes.

* Fri May 13 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev137-1
- Update to version 0.1.0.2.

* Tue May 10 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev%{rev}-1
- Initial package.

