%global debug_package %{nil}

Name:           pantheon-greeter
Summary:        Pantheon's LightDM Login Screen
Version:        3.1.0+rev%{rev}
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
* Sun Jun 18 2017 Fabio Valentini <decathorpe@gmail.com> - 3.1.0+rev565-1
- Update to latest snapshot.

* Thu Jun 08 2017 Fabio Valentini <decathorpe@gmail.com> - 3.1.0+rev563-1
- Update to latest snapshot.

* Thu Jun 08 2017 Fabio Valentini <decathorpe@gmail.com> - 3.1.0+rev560-1
- Update to latest snapshot.

* Tue Jun 06 2017 Fabio Valentini <decathorpe@gmail.com> - 3.1.0+rev555-1
- Update to latest snapshot.

* Mon Jun 05 2017 Fabio Valentini <decathorpe@gmail.com> - 3.1.0+rev553-1
- Update to latest snapshot.

* Mon May 22 2017 Fabio Valentini <decathorpe@gmail.com> - 3.1.0+rev551-1
- Update to latest snapshot.

* Thu May 11 2017 Fabio Valentini <decathorpe@gmail.com> - 3.1.0+rev549-1
- Update to latest snapshot.

* Sun Apr 30 2017 Fabio Valentini <decathorpe@gmail.com> - 3.1.0+rev548-1
- Update to latest snapshot.

* Mon Apr 24 2017 Fabio Valentini <decathorpe@gmail.com> - 3.1.0+rev547-1
- Update to latest snapshot.

* Thu Apr 20 2017 Fabio Valentini <decathorpe@gmail.com> - 3.1.0+rev546-1
- Update to latest snapshot.

* Thu Apr 20 2017 Fabio Valentini <decathorpe@gmail.com> - 3.1.0+rev545-1
- Update to latest snapshot.

* Mon Apr 17 2017 Fabio Valentini <decathorpe@gmail.com> - 3.1.0+rev544-1
- Update to latest snapshot.

* Mon Apr 17 2017 Fabio Valentini <decathorpe@gmail.com> - 3.1.0+rev543-1
- Update to latest snapshot.

* Wed Apr 05 2017 Fabio Valentini <decathorpe@gmail.com> - 3.1.0+rev538-1
- Update to latest snapshot.

* Wed Mar 22 2017 Fabio Valentini <decathorpe@gmail.com> - 3.1.0+rev537-1
- Update to latest snapshot.

* Sun Mar 19 2017 Fabio Valentini <decathorpe@gmail.com> - 3.1.0+rev536-1
- Update to latest snapshot.

* Wed Mar 15 2017 Fabio Valentini <decathorpe@gmail.com> - 3.1.0+rev535-1
- Update to latest snapshot.

* Tue Mar 14 2017 Fabio Valentini <decathorpe@gmail.com> - 3.1.0+rev534-1
- Update to latest snapshot.

* Thu Mar 09 2017 Fabio Valentini <decathorpe@gmail.com> - 3.1.0+rev533-1
- Update to latest snapshot.

* Thu Mar 02 2017 Fabio Valentini <decathorpe@gmail.com> - 3.1.0+rev532-1
- Update to latest snapshot.

* Mon Feb 27 2017 Fabio Valentini <decathorpe@gmail.com> - 3.1.0+rev531-1
- Update to latest snapshot.

* Sat Feb 25 2017 Fabio Valentini <decathorpe@gmail.com> - 3.1.0+rev530-1
- Update to latest snapshot.

* Mon Feb 13 2017 Fabio Valentini <decathorpe@gmail.com> - 3.1.0+rev529-1
- Update to latest snapshot.

* Sun Feb 12 2017 Fabio Valentini <decathorpe@gmail.com> - 3.1.0+rev528-1
- Update to latest snapshot.

* Fri Feb 10 2017 Fabio Valentini <decathorpe@gmail.com> - 3.1.0+rev527-1
- Update to latest snapshot.

* Sat Feb 04 2017 Fabio Valentini <decathorpe@gmail.com> - 3.1.0+rev526-1
- Update to latest snapshot.

* Thu Feb 02 2017 Fabio Valentini <decathorpe@gmail.com> - 3.1.0+rev525-1
- Update to latest snapshot.

* Wed Feb 01 2017 Fabio Valentini <decathorpe@gmail.com> - 3.1.0+rev524-1
- Update to version 3.1.0.

* Wed Feb 01 2017 Fabio Valentini <decathorpe@gmail.com> - 3.0+rev524-1
- Update to latest snapshot.

* Sat Jan 28 2017 Fabio Valentini <decathorpe@gmail.com> - 3.0+rev522-1
- Update to latest snapshot.

* Tue Jan 24 2017 Fabio Valentini <decathorpe@gmail.com> - 3.0+rev521-1
- Update to latest snapshot.

* Sat Jan 21 2017 Fabio Valentini <decathorpe@gmail.com> - 3.0+rev520-1
- Update to latest snapshot.

* Fri Jan 06 2017 Fabio Valentini <decathorpe@gmail.com> - 3.0+rev519-1
- Update to version 3.0.

* Thu Jan 05 2017 Fabio Valentini <decathorpe@gmail.com> - 3.0+rev518-1
- Update to version 3.0.

* Wed Jan 04 2017 Fabio Valentini <decathorpe@gmail.com> - 3.0+rev517-1
- Update to version 3.0.

* Tue Jan 03 2017 Fabio Valentini <decathorpe@gmail.com> - 3.0+rev516-1
- Update to version 3.0.

* Sun Jan 01 2017 Fabio Valentini <decathorpe@gmail.com> - 3.0+rev514-1
- Update to latest snapshot.

* Sat Dec 31 2016 Fabio Valentini <decathorpe@gmail.com> - 3.0+rev513-1
- Update to latest snapshot.

* Thu Dec 22 2016 Fabio Valentini <decathorpe@gmail.com> - 3.0+rev512-1
- Update to latest snapshot.

* Sun Dec 18 2016 Fabio Valentini <decathorpe@gmail.com> - 3.0+rev511-1
- Update to latest snapshot.

* Thu Dec 15 2016 Fabio Valentini <decathorpe@gmail.com> - 3.0+rev510-1
- Update to latest snapshot.

* Wed Dec 14 2016 Fabio Valentini <decathorpe@gmail.com> - 3.0+rev509-1
- Update to latest snapshot.

* Tue Dec 13 2016 Fabio Valentini <decathorpe@gmail.com> - 3.0+rev508-1
- Update to latest snapshot.

* Mon Dec 12 2016 Fabio Valentini <decathorpe@gmail.com> - 3.0+rev507-1
- Update to latest snapshot.

* Sun Dec 11 2016 Fabio Valentini <decathorpe@gmail.com> - 3.0+rev506-1
- Update to latest snapshot.

* Sat Dec 10 2016 Fabio Valentini <decathorpe@gmail.com> - 3.0+rev505-1
- Update to latest snapshot.

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


