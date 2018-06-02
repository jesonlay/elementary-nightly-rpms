%global srcname greeter
%global appname io.elementary.greeter

Name:           pantheon-greeter
Summary:        Pantheon's LightDM Login Screen
Version:        3.2.0+git%{date}.%{commit}
Release:        1%{?dist}
License:        GPLv3

URL:            https://github.com/elementary/%{srcname}
Source0:        %{name}-%{version}.tar.gz
Source1:        40-io.elementary.greeter.conf
Source2:        io.elementary.greeter.whitelist
Source3:        io.elementary.greeter.conf

# Remove gsettings stuff that's no longer there and causes crashes
Patch0:         00-disable-gsettings.patch

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  vala >= 0.26

BuildRequires:  mutter-devel

BuildRequires:  pkgconfig(clutter-gtk-1.0)
BuildRequires:  pkgconfig(gnome-desktop-3.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gdk-x11-3.0)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.11.6
BuildRequires:  pkgconfig(liblightdm-gobject-1) >= 1.2.1
BuildRequires:  pkgconfig(wingpanel-2.0)


Requires:       lightdm%{?_isa}
Requires:       wingpanel%{?_isa}

# Raleway font is used for interface elements
Requires:       impallari-raleway-fonts

# Runtime requirement for numlock capture
Requires:       numlockx

# Runtime requirement for hardcoded elementary's default wallpaper
Requires:       elementary-wallpapers


# All LightDM greeters provide this
Provides:       lightdm-greeter = 1.2

# Alternate, more descriptive names
Provides:       lightdm-%{name} = %{version}-%{release}
Provides:       lightdm-%{name}%{?_isa} = %{version}-%{release}


%description
Pantheon Greeter is a Pantheon-styled Login Screen for LightDM.


%prep
%autosetup -p1


%build
%meson
%meson_build


%install
%meson_install

%find_lang %{appname}

# Install LightDM configuration file
mkdir -p %{buildroot}%{_sysconfdir}/lightdm/lightdm.conf.d
install -pm 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/lightdm/lightdm.conf.d/

# Install wingpanel overrides for the greeter
mkdir -p %{buildroot}%{_sysconfdir}/wingpanel.d
install -pm 0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/wingpanel.d

# Install settings override for different wallpaper location on fedora
mkdir -p %{buildroot}%{_sysconfdir}/lightdm
install -pm 0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/lightdm/


%files -f %{appname}.lang
%license LICENSE

%config(noreplace) %{_sysconfdir}/lightdm/%{appname}.conf
%config(noreplace) %{_sysconfdir}/lightdm/lightdm.conf.d/40-%{appname}.conf
%config(noreplace) %{_sysconfdir}/wingpanel.d/%{appname}.whitelist

%{_bindir}/%{appname}-compositor

%{_sbindir}/%{appname}

%{_datadir}/xgreeters/%{appname}.desktop


%changelog
* Sat Jun 02 2018 Fabio Valentini <decathorpe@gmail.com> - 3.2.0+git180602.190307.ae5ef9da-1
- Update to latest snapshot.

* Sat Jun 02 2018 Fabio Valentini <decathorpe@gmail.com> - 3.2.0+git180602.163749.49a5421d-1
- Update to latest snapshot.

* Sat Jun 02 2018 Fabio Valentini <decathorpe@gmail.com> - 3.2.0+git180602.125217.f7400963-1
- Update to latest snapshot.

* Sat Jun 02 2018 Fabio Valentini <decathorpe@gmail.com> - 3.2.0+git180602.084733.e592fd5d-2
- Adapt to upstream dependency and file changes.

* Sat Jun 02 2018 Fabio Valentini <decathorpe@gmail.com> - 3.2.0+git180602.084733.e592fd5d-1
- Update to latest snapshot.

* Fri Jun 01 2018 Fabio Valentini <decathorpe@gmail.com> - 3.2.0+git180601.183749.176c31b4-2
- Adapt to upstream file changes.

* Fri Jun 01 2018 Fabio Valentini <decathorpe@gmail.com> - 3.2.0+git180601.183749.176c31b4-1
- Update to latest snapshot.

* Wed May 16 2018 Fabio Valentini <decathorpe@gmail.com> - 3.2.0+git180516.111907.4e73eefa-2
- Adapt to CMake -> meson switch.

* Wed May 16 2018 Fabio Valentini <decathorpe@gmail.com> - 3.2.0+git180516.111907.4e73eefa-1
- Update to latest snapshot.

* Tue May 15 2018 Fabio Valentini <decathorpe@gmail.com> - 3.2.0+git180515.123016.a1a44f31-2
- Adapt to upstream file changes.

* Tue May 15 2018 Fabio Valentini <decathorpe@gmail.com> - 3.2.0+git180515.123016.a1a44f31-1
- Update to latest snapshot.

* Sun May 13 2018 Fabio Valentini <decathorpe@gmail.com> - 3.2.0+git180510.171547.6411c087-2
- Add patch to fix wallpaper on greeter.

* Thu May 10 2018 Fabio Valentini <decathorpe@gmail.com> - 3.2.0+git180510.171547.6411c087-1
- Update to latest snapshot.

* Sun May 06 2018 Fabio Valentini <decathorpe@gmail.com> - 3.2.0+git180502.233957.140f32de-2
- Adapt patch to upstream changes.

* Thu May 03 2018 Fabio Valentini <decathorpe@gmail.com> - 3.2.0+git180502.233957.140f32de-1
- Update to latest snapshot.

* Sat Apr 21 2018 Fabio Valentini <decathorpe@gmail.com> - 3.2.0+git180421.001042.f88ab3f6-1
- Update to latest snapshot.

* Tue Apr 03 2018 Fabio Valentini <decathorpe@gmail.com> - 3.2.0+git180331.164404.e659ec47-1
- Update to latest snapshot.

* Tue Mar 27 2018 Fabio Valentini <decathorpe@gmail.com> - 3.2.0+git180327.162648.fb17673a-1
- Update to latest snapshot.

* Mon Mar 26 2018 Fabio Valentini <decathorpe@gmail.com> - 3.2.0+git180325.222053.b5249d19-1
- Update to latest snapshot.

* Sun Mar 11 2018 Fabio Valentini <decathorpe@gmail.com> - 3.2.0+git180311.071320.22831f41-1
- Update to latest snapshot.

* Sat Feb 24 2018 Fabio Valentini <decathorpe@gmail.com> - 3.2.0+git180223.205848.9b73c00f-1
- Update to latest snapshot.

* Fri Feb 09 2018 Fabio Valentini <decathorpe@gmail.com> - 3.2.0+git180209.004947.f5508b15-1
- Update to latest snapshot.

* Fri Jan 19 2018 Fabio Valentini <decathorpe@gmail.com> - 3.2.0+git180119.112013.1f101ad2-1
- Update to latest snapshot.

* Wed Jan 03 2018 Fabio Valentini <decathorpe@gmail.com> - 3.2.0+git171218.142123.940975c1-2
- Merge .spec file from fedora.

* Mon Dec 18 2017 Fabio Valentini <decathorpe@gmail.com> - 3.2.0+git171218.142123.940975c1-1
- Update to latest snapshot.

* Mon Nov 20 2017 Fabio Valentini <decathorpe@gmail.com> - 3.2.0+git171118.234650.1983fbe9-1
- Update to latest snapshot.

* Tue Nov 14 2017 Fabio Valentini <decathorpe@gmail.com> - 3.2.0+git171114.060754.4d0ec708-1
- Update to latest snapshot.

* Mon Sep 25 2017 Fabio Valentini <decathorpe@gmail.com> - 3.2.0+git170925.094744.552985ec-1
- Update to latest snapshot.

* Wed Sep 13 2017 Fabio Valentini <decathorpe@gmail.com> - 3.2.0+git170912.051756.cbd96db8-1
- Update to version 3.2.0.

* Tue Sep 12 2017 Fabio Valentini <decathorpe@gmail.com> - 3.1.0+rev587-1
- Update to latest snapshot.

* Wed Aug 23 2017 Fabio Valentini <decathorpe@gmail.com> - 3.1.0+rev586-1
- Update to latest snapshot.

* Fri Aug 18 2017 Fabio Valentini <decathorpe@gmail.com> - 3.1.0+rev585-1
- Update to latest snapshot.

* Wed Jul 26 2017 Fabio Valentini <decathorpe@gmail.com> - 3.1.0+rev584-1
- Update to latest snapshot.

* Mon Jul 24 2017 Fabio Valentini <decathorpe@gmail.com> - 3.1.0+rev583-1
- Update to latest snapshot.

* Wed Jul 12 2017 Fabio Valentini <decathorpe@gmail.com> - 3.1.0+rev579-1
- Update to latest snapshot.

* Sun Jul 02 2017 Fabio Valentini <decathorpe@gmail.com> - 3.1.0+rev577-1
- Update to latest snapshot.

* Thu Jun 29 2017 Fabio Valentini <decathorpe@gmail.com> - 3.1.0+rev576-1
- Update to latest snapshot.

* Sat Jun 24 2017 Fabio Valentini <decathorpe@gmail.com> - 3.1.0+rev575-1
- Update to latest snapshot.

* Mon Jun 19 2017 Fabio Valentini <decathorpe@gmail.com> - 3.1.0+rev573-1
- Update to latest snapshot.

* Mon Jun 19 2017 Fabio Valentini <decathorpe@gmail.com> - 3.1.0+rev572-1
- Update to latest snapshot.

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


