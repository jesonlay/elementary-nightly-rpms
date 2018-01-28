%global __provides_exclude_from ^%{_libdir}/switchboard/.*\\.so$

Name:           switchboard-plug-power
Summary:        Switchboard Power Plug
Version:        0.3.2+git%{date}.%{commit}
Release:        1%{?dist}
License:        GPLv3

URL:            https://github.com/elementary/%{name}
Source0:        %{name}-%{version}.tar.gz

# Add patch to not use (dysfunctional) elementary-dpms-helper
Patch0:         00-no-e-dpms-helper.patch

BuildRequires:  cmake
BuildRequires:  gettext
BuildRequires:  vala >= 0.30.0
BuildRequires:  vala-tools

BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  pkgconfig(gnome-settings-daemon)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  pkgconfig(switchboard-2.0)

Requires:       dbus

Supplements:    switchboard%{?_isa}


%description
Control system power consumption with this Switchboard preference plug.


%prep
%autosetup -p1


%build
mkdir build && pushd build
%cmake ..

# Parallel builds hit a race condition and fail
# https://github.com/elementary/switchboard-plug-power/issues/40
make
popd


%install
pushd build
%make_install
popd

%find_lang pantheon-power-plug


%files -f pantheon-power-plug.lang
%doc README.md
%license COPYING

%config(noreplace) %{_sysconfdir}/dbus-1/system.d/io.elementary.logind.helper.conf

%{_libdir}/switchboard/hardware/pantheon-power/

%{_datadir}/dbus-1/system-services/io.elementary.logind.helper.service
%{_datadir}/polkit-1/actions/org.pantheon.switchboard.power.policy


%changelog
* Sun Jan 28 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180128.020222.ced39b8c-1
- Update to latest snapshot.

* Sat Jan 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180127.202258.4d6181dd-1
- Update to latest snapshot.

* Fri Jan 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180125.102055.8de48329-2
- Adapt patch to upstream changes.

* Thu Jan 25 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180125.102055.8de48329-1
- Update to latest snapshot.

* Wed Jan 24 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180124.140355.868ba346-1
- Update to latest snapshot.

* Wed Jan 24 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180124.062628.52aeaedf-1
- Update to latest snapshot.

* Tue Jan 23 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180123.204619.aeab31bf-1
- Update to latest snapshot.

* Tue Jan 23 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180123.170619.e3a02b71-1
- Update to latest snapshot.

* Tue Jan 23 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180123.162207.7f5f8eaa-1
- Update to latest snapshot.

* Tue Jan 23 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180123.155523.9c651f38-1
- Update to latest snapshot.

* Tue Jan 23 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180123.000558.93fb5a4b-1
- Update to latest snapshot.

* Mon Jan 22 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180122.091505.5327d3fa-1
- Update to latest snapshot.

* Mon Jan 22 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git180122.061941.4330562b-1
- Update to latest snapshot.

* Fri Jan 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git171112.174647.cf8fd1ca-2
- Merge .spec file from elementary-stable.

* Sun Nov 12 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git171112.174647.cf8fd1ca-1
- Update to latest snapshot.

* Sat Oct 07 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git171007.070336.965c050e-1
- Update to latest snapshot.

* Sun Sep 24 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git170924.001034.f80326f4-1
- Update to latest snapshot.

* Sat Sep 23 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git170923.185712.da8d5c6f-1
- Update to latest snapshot.

* Sat Aug 19 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git170817.000746.b0739ce5-1
- Update to latest snapshot.

* Sun Aug 06 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git170719.185928.fd6e0bf8-2
- Add patch to remove usage and dependency on e-dpms-helper.

* Wed Jul 19 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.2+git170719.185928.fd6e0bf8-1
- Update to version 0.3.2.

* Wed Jul 19 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git170719.185928.fd6e0bf8-1
- Update to latest snapshot.

* Sat Jul 15 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git170715.120953.ef1e981a-1
- Update to latest snapshot.

* Sun Jul 02 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git170702.171704.de550755-1
- Update to latest snapshot.

* Sun Jul 02 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git170702.110138.955fcc93-1
- Update to latest snapshot.

* Wed Jun 21 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git170621.170427.27ca0dbc-1
- Update to latest snapshot.

* Wed Jun 21 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git170621.163313.8e244d22-1
- Update to latest snapshot.

* Tue Jun 20 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git170619.111204.64d06d11-2
- Adapt to upstream file changes.

* Mon Jun 19 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git170619.111204.64d06d11-1
- Update to latest snapshot.

* Mon Jun 19 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git170619.064115.e60f522f-1
- Update to latest snapshot.

* Sun Jun 18 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git170617.160328.af784cd4-1
- Update to latest snapshot.

* Sat Jun 03 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git170603.180424.f7bb17b3-1
- Update to latest snapshot.

* Sat Jun 03 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git170603.175305.4b646925-1
- Update to latest snapshot.

* Fri Jun 02 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git170602.180706.63ecc031-1
- Update to latest snapshot.

* Fri Jun 02 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git170602.173926.4a22ba34-1
- Update to latest snapshot.

* Thu Jun 01 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git170601.211203.dd167ce2-1
- Update to latest snapshot.

* Thu Jun 01 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git170601.192843.f127a598-1
- Update to latest snapshot.

* Thu Jun 01 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git170601.012014.97d7184c-1
- Update to latest snapshot.

* Wed May 31 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git170530.213003.d991eb14-1
- Update to latest snapshot.

* Sun May 21 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git170521.211443.06578eb5-1
- Update to latest snapshot.

* Fri May 12 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.1+git170511.073106.5ce5bdfe-1
- Update to version 0.3.1.

* Thu May 11 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3+rev423-1
- Update to latest snapshot.

* Wed May 10 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3+rev422-1
- Update to latest snapshot.

* Tue Apr 25 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3+rev421-1
- Update to latest snapshot.

* Wed Apr 19 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3+rev417-1
- Update to latest snapshot.

* Fri Apr 14 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3+rev416-1
- Update to latest snapshot.

* Mon Apr 10 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3+rev415-1
- Update to latest snapshot.

* Wed Apr 05 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3+rev414-1
- Update to latest snapshot.

* Sun Mar 19 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3+rev413-1
- Update to latest snapshot.

* Wed Mar 15 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3+rev412-1
- Update to latest snapshot.

* Tue Mar 14 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3+rev411-1
- Update to latest snapshot.

* Thu Mar 02 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3+rev408-1
- Update to latest snapshot.

* Mon Feb 27 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3+rev407-1
- Update to latest snapshot.

* Mon Feb 20 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3+rev406-1
- Update to latest snapshot.

* Mon Feb 13 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3+rev405-1
- Update to latest snapshot.

* Sun Feb 12 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3+rev404-1
- Update to latest snapshot.

* Sat Feb 11 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3+rev403-1
- Update to latest snapshot.

* Wed Feb 08 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3+rev402-1
- Update to latest snapshot.

* Mon Jan 30 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3+rev401-1
- Update to latest snapshot.

* Sun Jan 29 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3+rev400-1
- Update to latest snapshot.

* Sat Jan 28 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3+rev399-1
- Update to latest snapshot.

* Fri Jan 27 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3+rev398-1
- Update to latest snapshot.

* Thu Jan 26 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3+rev397-1
- Update to latest snapshot.

* Tue Jan 24 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3+rev396-1
- Update to latest snapshot.

* Tue Jan 17 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3+rev395-1
- Update to latest snapshot.

* Mon Jan 09 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3+rev394-1
- Update to version 0.3.

* Sun Jan 08 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3+rev393-1
- Update to version 0.3.

* Sun Jan 01 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3+rev392-1
- Update to latest snapshot.

* Sat Dec 31 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3+rev391-1
- Update to latest snapshot.

* Wed Dec 28 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3+rev390-1
- Update to latest snapshot.

* Tue Dec 27 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3+rev389-1
- Update to latest snapshot.

* Mon Dec 26 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3+rev388-1
- Update to latest snapshot.

* Sun Dec 25 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3+rev387-1
- Update to latest snapshot.

* Sat Dec 24 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3+rev386-1
- Update to latest snapshot.

* Tue Dec 20 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3+rev385-1
- Update to latest snapshot.

* Sat Dec 17 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3+rev384-1
- Update to latest snapshot.

* Thu Dec 15 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3+rev383-1
- Update to latest snapshot.

* Wed Dec 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3+rev382-1
- Update to latest snapshot.

* Wed Dec 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3+rev381-1
- Update to latest snapshot.

* Tue Dec 13 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3+rev380-1
- Update to latest snapshot.

* Mon Dec 12 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3+rev379-1
- Update to latest snapshot.

* Sun Dec 11 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3+rev378-1
- Update to latest snapshot.

* Sat Dec 10 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3+rev377-1
- Update to latest snapshot.

* Fri Dec 09 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3+rev376-1
- Update to latest snapshot.

* Fri Dec 02 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3+rev375-1
- Update to latest snapshot.

* Thu Dec 01 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3+rev374-1
- Update to latest snapshot.

* Wed Nov 30 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3+rev373-1
- Update to latest snapshot.

* Tue Nov 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3+rev372-1
- Update to latest snapshot.

* Mon Nov 28 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3+rev371-1
- Update to latest snapshot.

* Wed Nov 23 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3+rev370-1
- Update to version 0.3.


