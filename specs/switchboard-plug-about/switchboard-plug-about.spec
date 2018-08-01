%global __provides_exclude_from ^%{_libdir}/switchboard/.*\\.so$

Name:           switchboard-plug-about
Summary:        Switchboard System Information plug
Version:        0.2.5+git%{date}.%{commit}
Release:        1%{?dist}
License:        GPLv3+

URL:            https://github.com/elementary/%{name}
Source0:        %{name}-%{version}.tar.gz

# Use official logo in the system details view
Patch0:         00-fedora-logo.patch

BuildRequires:  gettext
BuildRequires:  meson
BuildRequires:  vala >= 0.22.0
BuildRequires:  vala-tools

BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(switchboard-2.0)

Supplements:    switchboard%{?_isa}

Requires:       system-logos


%description
This switchboard plug shows system information.


%prep
%autosetup -p1


%build
%meson
%meson_build


%install
%meson_install

%find_lang about-plug


%files -f about-plug.lang
%doc README.md
%license COPYING

%{_libdir}/switchboard/hardware/libabout.so


%changelog
* Wed Aug 01 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git180801.160842.ab79dee6-1
- Update to latest snapshot.

* Sat Jul 21 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git180721.000732.4d0e3468-1
- Update to latest snapshot.

* Fri Jul 20 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git180720.210746.9553be05-1
- Update to latest snapshot.

* Tue Jul 17 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git180716.154045.cae96744-1
- Update to latest snapshot.

* Thu Jul 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git180704.231230.1676a600-1
- Update to latest snapshot.

* Wed Jul 04 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git180703.192419.1625519e-1
- Update to latest snapshot.

* Wed Jun 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git180613.000734.4e1db225-1
- Update to latest snapshot.

* Tue Jun 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git180612.074611.2a91d1b0-1
- Update to latest snapshot.

* Sun Jun 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git180610.001149.dc76d5ea-1
- Update to latest snapshot.

* Fri Jun 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5+git180608.131457.8c0f48cf-1
- Update to version 0.2.5.

* Fri Jun 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180608.131457.8c0f48cf-1
- Update to latest snapshot.

* Mon Jun 04 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180604.022534.cd8052ef-1
- Update to latest snapshot.

* Thu May 31 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180531.000244.4acb2d28-1
- Update to latest snapshot.

* Wed May 30 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180530.000344.52746f41-1
- Update to latest snapshot.

* Tue May 29 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180529.131441.43f30909-1
- Update to latest snapshot.

* Mon May 28 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180528.000255.57bd5f4d-1
- Update to latest snapshot.

* Sun May 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180527.115220.7932cbbe-1
- Update to latest snapshot.

* Sat May 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180525.203545.d3729a19-1
- Update to latest snapshot.

* Thu May 24 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180520.151824.2c0ab680-1
- Update to latest snapshot.

* Fri May 18 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180518.000735.5000ad07-1
- Update to latest snapshot.

* Thu May 17 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180517.000412.3e525fac-1
- Update to latest snapshot.

* Wed May 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180516.135310.219d7f44-1
- Update to latest snapshot.

* Sun May 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180513.095158.356eb51f-1
- Update to latest snapshot.

* Sat May 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180512.001137.6067dd7c-1
- Update to latest snapshot.

* Thu May 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180510.171821.2e39e72e-1
- Update to latest snapshot.

* Thu May 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180510.161028.98908cdf-1
- Update to latest snapshot.

* Thu May 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180510.000911.70337c0c-1
- Update to latest snapshot.

* Tue May 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180508.152058.f16e0ce5-1
- Update to latest snapshot.

* Tue May 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180507.213131.1be0644e-1
- Update to latest snapshot.

* Mon May 07 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180507.000253.e27ce7d0-1
- Update to latest snapshot.

* Sun May 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180506.001005.c7ca86ed-1
- Update to latest snapshot.

* Thu May 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180503.054500.3ae3004e-1
- Update to latest snapshot.

* Tue May 01 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180501.105713.f1d95571-1
- Update to latest snapshot.

* Tue May 01 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180501.095430.22cd1d91-1
- Update to latest snapshot.

* Tue May 01 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180501.042358.eaee4103-1
- Update to latest snapshot.

* Tue Apr 24 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180424.095041.ee51234b-1
- Update to latest snapshot.

* Mon Apr 09 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180409.000457.2a2f5b71-1
- Update to latest snapshot.

* Sun Apr 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180408.100032.02858026-1
- Update to latest snapshot.

* Wed Apr 04 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180404.000708.9b4032eb-1
- Update to latest snapshot.

* Tue Apr 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180402.105716.dfd0bffc-1
- Update to latest snapshot.

* Mon Mar 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180326.000856.badcac9a-1
- Update to latest snapshot.

* Sun Mar 25 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180324.174630.768b7ffc-1
- Update to latest snapshot.

* Tue Mar 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180313.025809.878b4dcd-1
- Update to latest snapshot.

* Mon Mar 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180312.154247.8eedd3f5-1
- Update to latest snapshot.

* Mon Mar 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180311.222526.b77f0493-1
- Update to latest snapshot.

* Sun Mar 11 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180311.094958.a55c45de-1
- Update to latest snapshot.

* Sat Mar 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180310.162106.c692d41b-1
- Update to latest snapshot.

* Sat Mar 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180310.000416.fd19551e-1
- Update to latest snapshot.

* Fri Mar 09 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180309.082724.802494b9-1
- Update to latest snapshot.

* Thu Mar 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180308.193148.37142d4c-1
- Update to latest snapshot.

* Thu Mar 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180308.180433.b314ac35-1
- Update to latest snapshot.

* Thu Mar 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180308.151649.c2a1a877-1
- Update to latest snapshot.

* Mon Mar 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180305.115050.a207098e-1
- Update to latest snapshot.

* Wed Feb 28 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180228.105809.51f68389-1
- Update to latest snapshot.

* Mon Feb 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180226.201759.559a1d2d-1
- Update to latest snapshot.

* Sun Feb 25 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180225.121246.4b751a9d-1
- Update to latest snapshot.

* Sun Feb 25 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180225.000927.ee1153eb-1
- Update to latest snapshot.

* Sat Feb 24 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180224.113435.5f0030c9-1
- Update to latest snapshot.

* Sat Feb 24 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180224.000412.12612fb3-1
- Update to latest snapshot.

* Fri Feb 23 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180223.184238.00d0a928-1
- Update to latest snapshot.

* Fri Feb 23 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180221.221857.fc251650-2
- Adapt to cmake -> meson switch.

* Thu Feb 22 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180221.221857.fc251650-1
- Update to latest snapshot.

* Wed Feb 21 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180221.144707.f2506d79-1
- Update to latest snapshot.

* Wed Feb 21 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180221.074327.6423fa39-1
- Update to latest snapshot.

* Tue Feb 20 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180220.212715.ae2f2225-1
- Update to latest snapshot.

* Sun Feb 18 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180218.110914.ffc3cd35-1
- Update to latest snapshot.

* Tue Feb 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180213.201203.eea5ebf6-1
- Update to latest snapshot.

* Mon Feb 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180205.001138.de9123ea-1
- Update to latest snapshot.

* Sat Jan 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180117.181133.6877ed0b-1
- Update to latest snapshot.

* Wed Jan 17 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180117.181130.1d19504f-1
- Update to latest snapshot.

* Mon Jan 15 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180114.114129.1c705944-2
- Adapt patch for upstream changes.

* Mon Jan 15 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180114.114129.1c705944-1
- Update to latest snapshot.

* Thu Jan 04 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git170921.170550.974d3f19-2
- Merge .spec file from fedora.

* Fri Nov 10 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git170921.170550.974d3f19-1
- Initial package.


