%global __provides_exclude_from ^%{_libdir}/switchboard/.*\\.so$

Name:           switchboard-plug-networking
Summary:        Switchboard Networking plug
Version:        0.1.1+git%{date}.%{commit}
Release:        1%{?dist}
License:        GPLv3+

URL:            https://github.com/elementary/%{name}
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  gettext
BuildRequires:  meson
BuildRequires:  vala >= 0.22.0
BuildRequires:  vala-tools

BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libnm)
BuildRequires:  pkgconfig(libnma)
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  pkgconfig(switchboard-2.0)

Supplements:    (switchboard%{?_isa} and NetworkManager%{?_isa})


%description
A switchboard plug for configuring available networks.


%prep
%autosetup


%build
%meson
%meson_build


%install
%meson_install

%find_lang networking-plug


%files -f networking-plug.lang
%doc README.md
%license COPYING

%{_libdir}/switchboard/network/libnetworking.so


%changelog
* Sun Jun 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180603.070643.2979895a-1
- Update to latest snapshot.

* Sat Jun 02 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180602.000624.3c7405de-1
- Update to latest snapshot.

* Fri Jun 01 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180601.000812.27ce4efa-1
- Update to latest snapshot.

* Thu May 31 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180531.000309.bd3a7f68-1
- Update to latest snapshot.

* Wed May 30 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180530.123946.10841a56-1
- Update to latest snapshot.

* Wed May 30 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180530.035237.8bac34f0-1
- Update to latest snapshot.

* Tue May 29 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180529.001243.3bb1accd-1
- Update to latest snapshot.

* Mon May 28 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180528.071912.e01890ce-1
- Update to latest snapshot.

* Sun May 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180527.000550.28a5c1ef-1
- Update to latest snapshot.

* Sat May 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180525.164147.99c39b91-1
- Update to latest snapshot.

* Thu May 24 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180524.001038.d9c46139-1
- Update to latest snapshot.

* Mon May 14 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180514.000238.ebdabac6-1
- Update to latest snapshot.

* Sun May 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180513.101313.4b2cc42a-1
- Update to latest snapshot.

* Sat May 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180512.001159.489d3a22-1
- Update to latest snapshot.

* Fri May 11 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180511.032229.5e413d5a-1
- Update to latest snapshot.

* Thu May 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180510.172051.0dac2496-1
- Update to latest snapshot.

* Thu May 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180510.120312.51fd5d12-1
- Update to latest snapshot.

* Thu May 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180510.000923.7e85764b-1
- Update to latest snapshot.

* Mon May 07 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180507.000312.dc35b4fc-1
- Update to latest snapshot.

* Sun May 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180506.001018.d26fdb01-1
- Update to latest snapshot.

* Thu May 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180503.080152.bf4ae949-1
- Update to latest snapshot.

* Tue May 01 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180429.115218.22a97210-1
- Update to latest snapshot.

* Thu Apr 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180426.000345.4af6030e-1
- Update to latest snapshot.

* Tue Apr 24 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180424.211516.9652e34e-1
- Update to latest snapshot.

* Sat Apr 21 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180421.001132.77ff7438-1
- Update to latest snapshot.

* Sun Apr 15 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180415.001024.9420c053-1
- Update to latest snapshot.

* Sat Apr 14 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180414.124353.829565bc-1
- Update to latest snapshot.

* Sun Apr 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180406.080741.c9f9e0e8-1
- Update to latest snapshot.

* Thu Apr 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180405.143429.15045faa-1
- Update to latest snapshot.

* Wed Apr 04 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180404.000717.85120596-1
- Update to latest snapshot.

* Tue Apr 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180403.142806.f598e709-1
- Update to latest snapshot.

* Wed Mar 28 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180328.195243.dda97281-1
- Update to latest snapshot.

* Wed Mar 28 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180328.090437.b9ba8a04-1
- Update to latest snapshot.

* Tue Mar 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180327.162412.93e3de4d-1
- Update to latest snapshot.

* Mon Mar 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180326.174426.9ef566f4-1
- Update to latest snapshot.

* Mon Mar 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180326.072945.ea9b9199-1
- Update to latest snapshot.

* Sun Mar 25 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180325.211748.41948d16-1
- Update to latest snapshot.

* Sun Mar 25 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180325.000928.d4de991c-1
- Update to latest snapshot.

* Tue Mar 20 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180320.001157.c39f47b7-1
- Update to latest snapshot.

* Wed Mar 14 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180314.000226.5d059510-1
- Update to latest snapshot.

* Mon Mar 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180312.001005.a2e23c60-1
- Update to latest snapshot.

* Fri Mar 09 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180309.000611.ee5007e2-1
- Update to latest snapshot.

* Thu Mar 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180308.000909.b8ec6509-2
- Adapt to dependency changes.

* Thu Mar 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180308.000909.b8ec6509-1
- Update to latest snapshot.

* Tue Feb 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180227.000415.2ee05bce-1
- Update to latest snapshot.

* Mon Feb 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180226.094153.a2c850f6-1
- Update to latest snapshot.

* Sat Feb 24 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180223.125025.3810943b-2
- Adapt to cmake -> meson switch.

* Fri Feb 23 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180223.125025.3810943b-1
- Update to latest snapshot.

* Wed Feb 21 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180220.225803.00b630b3-1
- Update to latest snapshot.

* Tue Feb 20 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180220.215028.13ba7908-1
- Update to latest snapshot.

* Sun Feb 18 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180218.200533.c52183a1-1
- Update to latest snapshot.

* Sat Feb 17 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180217.101014.5af48c8f-1
- Update to latest snapshot.

* Mon Feb 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180211.000853.f2dfaec0-1
- Update to latest snapshot.

* Fri Feb 09 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180209.000246.d68ac879-1
- Update to latest snapshot.

* Thu Feb 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180208.220332.2e0f5d0b-1
- Update to latest snapshot.

* Mon Feb 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180205.001150.3d1bce13-1
- Update to latest snapshot.

* Thu Feb 01 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180201.000924.d343b692-1
- Update to latest snapshot.

* Mon Jan 29 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180129.000243.f2ef1946-1
- Update to latest snapshot.

* Sat Jan 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180118.000240.5265ea66-1
- Update to latest snapshot.

* Fri Jan 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180105.085339.b1094cb4-1
- Update to latest snapshot.

* Thu Jan 04 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180103.010504.5910cd45-2
- Merge .spec file from fedora.

* Wed Jan 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180103.010504.5910cd45-1
- Update to latest snapshot.

* Sat Dec 30 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git171229.230757.cfa74410-1
- Update to latest snapshot.

* Wed Dec 27 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git171227.173136.e1bb1bc5-1
- Update to latest snapshot.

* Tue Dec 26 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git171226.174250.53810d6a-1
- Update to latest snapshot.

* Sun Dec 24 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git171222.220023.5a5867be-2
- Adapt to upstream dependency changes.

* Sun Dec 24 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git171222.220023.5a5867be-1
- Update to latest snapshot.

* Wed Dec 20 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git171220.181623.c8ca88b0-1
- Update to latest snapshot.

* Mon Nov 20 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git171118.235353.8e23d341-1
- Update to latest snapshot.

* Fri Nov 17 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git171117.184103.adae98e2-1
- Update to latest snapshot.

* Thu Nov 02 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git171102.164146.382f335a-1
- Update to latest snapshot.

* Fri Oct 27 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git171027.154651.d36d298f-1
- Update to latest snapshot.

* Thu Oct 26 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git171026.172718.a8b97c55-1
- Update to latest snapshot.

* Wed Oct 25 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git171025.143830.b20434d6-1
- Update to latest snapshot.

* Wed Oct 25 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git171024.181951.59b079bd-1
- Update to latest snapshot.

* Tue Oct 24 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git171024.000054.03d3091f-1
- Update to latest snapshot.

* Mon Oct 23 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git171023.183001.c7e0308a-1
- Update to latest snapshot.

* Mon Oct 02 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git171002.185929.b49a6155-1
- Update to latest snapshot.

* Mon Oct 02 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git171002.143240.914b8935-1
- Update to latest snapshot.

* Fri Sep 22 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git170922.000642.b649a59f-1
- Update to latest snapshot.

* Sat Sep 16 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git170916.000221.e500be8d-1
- Update to latest snapshot.

* Fri Sep 15 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git170915.095826.284e1174-1
- Update to version 0.1.1.

* Fri Sep 15 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev504-1
- Update to latest snapshot.

* Sat Aug 19 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev503-1
- Update to latest snapshot.

* Sat Jul 15 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev501-1
- Update to latest snapshot.

* Sun Jul 02 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev495-1
- Update to latest snapshot.

* Wed Jun 21 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev491-1
- Update to latest snapshot.

* Sun Jun 18 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev490-1
- Update to latest snapshot.

* Tue May 23 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev384-1
- Update to latest snapshot.

* Sat May 06 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev383-1
- Update to latest snapshot.

* Tue Apr 25 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev382-1
- Update to latest snapshot.

* Wed Apr 05 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev381-1
- Update to latest snapshot.

* Wed Mar 22 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev380-1
- Update to latest snapshot.

* Sun Mar 19 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev379-1
- Update to latest snapshot.

* Tue Feb 28 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev378-1
- Update to latest snapshot.

* Thu Feb 23 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev377-1
- Update to latest snapshot.

* Sat Feb 18 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev376-1
- Update to latest snapshot.

* Mon Feb 13 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev375-1
- Update to latest snapshot.

* Sun Feb 12 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev374-1
- Update to latest snapshot.

* Sat Feb 11 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev373-1
- Update to latest snapshot.

* Fri Jan 27 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev372-1
- Update to latest snapshot.

* Thu Jan 26 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev371-1
- Update to latest snapshot.

* Wed Jan 25 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev370-1
- Update to latest snapshot.

* Sat Jan 21 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev369-1
- Update to latest snapshot.

* Wed Jan 18 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev368-1
- Update to latest snapshot.

* Mon Jan 16 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev367-1
- Update to latest snapshot.

* Wed Jan 11 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev366-1
- Update to version 0.1.0.3.

* Tue Jan 10 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev365-1
- Update to version 0.1.0.3.

* Wed Jan 04 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev364-1
- Update to version 0.1.0.3.

* Tue Jan 03 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev363-1
- Update to version 0.1.0.3.

* Sun Jan 01 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev362-1
- Update to latest snapshot.

* Sun Jan 01 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev361-1
- Update to latest snapshot.

* Sat Dec 31 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev360-1
- Update to latest snapshot.

* Fri Dec 30 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev359-1
- Update to latest snapshot.

* Thu Dec 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev358-1
- Update to latest snapshot.

* Tue Dec 27 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev356-1
- Update to latest snapshot.

* Mon Dec 26 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev355-1
- Update to latest snapshot.

* Sat Dec 24 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev354-1
- Update to latest snapshot.

* Fri Dec 23 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev353-1
- Update to latest snapshot.

* Fri Dec 23 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev352-1
- Update to latest snapshot.

* Wed Dec 21 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev351-1
- Update to latest snapshot.

* Tue Dec 20 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev350-1
- Update to latest snapshot.

* Fri Dec 16 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev349-1
- Update to latest snapshot.

* Thu Dec 15 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev348-1
- Update to latest snapshot.

* Wed Dec 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev347-1
- Update to latest snapshot.

* Wed Dec 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev346-1
- Update to latest snapshot.

* Wed Dec 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev345-1
- Update to latest snapshot.

* Tue Dec 13 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev344-1
- Update to latest snapshot.

* Mon Dec 12 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev343-1
- Update to latest snapshot.

* Sun Dec 11 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev342-1
- Update to latest snapshot.

* Sat Dec 10 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev341-1
- Update to latest snapshot.

* Fri Dec 09 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev340-1
- Update to version 0.1.0.3.


