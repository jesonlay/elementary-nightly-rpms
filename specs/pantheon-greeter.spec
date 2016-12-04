%global debug_package %{nil}

Name:           pantheon-greeter
Summary:        Pantheon's LightDM Login Screen
Version:        3.0+rev%{rev}
Release:        1%{?dist}
License:        GPLv3
URL:            http://launchpad.net/pantheon-greeter

Source0:        %{name}-%{version}.tar.gz
Source1:        %{name}.conf

# From http://bazaar.launchpad.net/~elementary-os/pantheon-greeter/deb-packaging/files/head:/debian/
Source2:        40-lightdm-pantheon-greeter.conf
Source3:        pantheon-greeter.whitelist

BuildRequires:  cmake
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  pkgconfig
BuildRequires:  vala >= 0.26

BuildRequires:  pkgconfig(clutter-gtk-1.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gdk-x11-3.0)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.11.6
BuildRequires:  pkgconfig(liblightdm-gobject-1) >= 1.2.1
BuildRequires:  pkgconfig(wingpanel-2.0)


# All LightDM greeters provide this
Provides:       lightdm-greeter = 1.2

# Alternate, more descriptive names
Provides:       lightdm-%{name} = %{version}-%{release}
Provides:       lightdm-%{name}%{?_isa} = %{version}-%{release}

# Runtime requirement for numlock capture
Requires:       numlockx


%description
Pantheon's LightDM Login Screen

Designed for elementary OS.


%prep
%autosetup


%build
mkdir build && cd build
%cmake ..
%make_build


%install
pushd build
%make_install
popd

%find_lang pantheon-greeter

mkdir -p %{buildroot}%{_sysconfdir}/lightdm/lightdm.conf.d
install -pm 0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/lightdm/lightdm.conf.d/

mkdir -p %{buildroot}%{_sysconfdir}/wingpanel.d
install -pm 0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/wingpanel.d


%files -f pantheon-greeter.lang
%{_sbindir}/pantheon-greeter

%config(noreplace) %{_sysconfdir}/lightdm/pantheon-greeter.conf
%config(noreplace) %{_sysconfdir}/lightdm/lightdm.conf.d/40-lightdm-pantheon-greeter.conf
%config(noreplace) %{_sysconfdir}/wingpanel.d/pantheon-greeter.whitelist

%{_datadir}/pantheon-greeter/
%{_datadir}/xgreeters/pantheon-greeter.desktop


%changelog
* Sun Dec 04 2016 Fabio Valentini <decathorpe@gmail.com> - 3.0+rev504-1
- Update to latest snapshot.

* Fri Dec 02 2016 Fabio Valentini <decathorpe@gmail.com> - 3.0+rev502-1
- Update to latest snapshot.

* Thu Dec 01 2016 Fabio Valentini <decathorpe@gmail.com> - 3.0+rev501-1
- Update to latest snapshot.

* Sun Nov 27 2016 Fabio Valentini <decathorpe@gmail.com> - 3.0+rev500-2
- Add missing configuration files.
- Add missing Provides and Requires.

* Sat Nov 19 2016 Fabio Valentini <decathorpe@gmail.com> - 3.0+rev500-1
- Update to snapshots of version 3.0.

* Sat Nov 19 2016 Fabio Valentini <decathorpe@gmail.com> - 3.0-1
- Update to version 3.0.


