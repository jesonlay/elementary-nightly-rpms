Summary:        The terminal of the 21st century.
Name:           pantheon-terminal
Version:        0.4.3+git%{date}.%{commit}
Release:        1%{?dist}
License:        LGPLv3
URL:            http://launchpad.net/pantheon-terminal

Source0:        %{name}-%{version}.tar.gz
Source1:        %{name}.conf

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig
BuildRequires:  vala

BuildRequires:  pkgconfig(gdk-3.0)
BuildRequires:  pkgconfig(granite) >= 0.3.0
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.9.10
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(vte-2.91)


%description
A super lightweight, beautiful, and simple terminal. It's designed to be
setup with sane defaults and little to no configuration. It's just a
terminal, nothing more, nothing less.


%prep
%autosetup


%build
mkdir build && pushd build
%cmake ..
%make_build
popd


%install
pushd build
%make_install
popd

%find_lang io.elementary.terminal

mv %{buildroot}/%{_datadir}/metainfo %{buildroot}/%{_datadir}/appdata


%check
desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/org.pantheon.terminal.desktop

desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/open-pantheon-terminal-here.desktop

appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/appdata/io.elementary.terminal.appdata.xml || :


%files -f io.elementary.terminal.lang
%doc AUTHORS README.md
%license COPYING

%{_bindir}/io.elementary.terminal

%{_datadir}/appdata/io.elementary.terminal.appdata.xml
%{_datadir}/applications/open-pantheon-terminal-here.desktop
%{_datadir}/applications/org.pantheon.terminal.desktop
%{_datadir}/glib-2.0/schemas/io.elementary.terminal.gschema.xml
%{_datadir}/io.elementary.terminal/


%changelog
* Mon Nov 20 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git171119.000915.e6d7aa76-1
- Update to latest snapshot.

* Sat Nov 18 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git171118.194509.2531af14-1
- Update to latest snapshot.

* Tue Nov 14 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git171113.210637.313fc34d-1
- Update to latest snapshot.

* Sun Nov 05 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git171105.175602.e7355274-1
- Update to latest snapshot.

* Fri Nov 03 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git171103.000113.bebc5a72-1
- Update to latest snapshot.

* Thu Nov 02 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git171102.101012.0ceb654e-1
- Update to latest snapshot.

* Wed Oct 25 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git171025.001014.302f1aae-1
- Update to latest snapshot.

* Tue Oct 24 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git171024.173602.1c633396-1
- Update to latest snapshot.

* Tue Oct 24 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git171024.161831.8788f6a7-1
- Update to latest snapshot.

* Tue Oct 03 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git171003.192137.fc24592d-1
- Update to latest snapshot.

* Mon Oct 02 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git171001.211730.71ffe762-1
- Update to latest snapshot.

* Thu Sep 28 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git170928.140848.185ef079-1
- Update to latest snapshot.

* Wed Sep 27 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git170927.162458.3f62e3d0-1
- Update to latest snapshot.

* Wed Sep 06 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git170906.000359.9da2d9ca-1
- Update to latest snapshot.

* Tue Sep 05 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git170905.204712.5f159b82-1
- Update to latest snapshot.

* Tue Aug 29 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git170829.000644.55e99bd0-1
- Update to latest snapshot.

* Mon Aug 28 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git170828.160548.c7f2f074-1
- Update to latest snapshot.

* Wed Aug 16 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git170816.172458.23190cb3-1
- Update to latest snapshot.

* Tue Aug 15 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git170815.003559.89c3beea-1
- Update to latest snapshot.

* Mon Aug 14 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git170814.000940.f89a59db-1
- Update to latest snapshot.

* Sun Aug 13 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git170813.155958.34409f55-1
- Update to latest snapshot.

* Sun Aug 13 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git170812.022200.6ae6d898-2
- Adapt to upstream file changes.

* Sat Aug 12 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git170812.022200.6ae6d898-1
- Update to latest snapshot.

* Fri Aug 11 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git170811.023138.3edbf907-1
- Update to latest snapshot.

* Thu Aug 10 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git170810.155924.226cf8b1-1
- Update to latest snapshot.

* Wed Aug 09 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git170809.181347.0009eb8e-2
- Adapt to upstream file changes.

* Wed Aug 09 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git170809.181347.0009eb8e-1
- Update to latest snapshot.

* Wed Aug 09 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git170809.153839.5c75fe25-1
- Update to latest snapshot.

* Tue Aug 08 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git170808.202249.0e2d2952-1
- Update to latest snapshot.

* Wed Aug 02 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git170802.000356.2d14c170-1
- Update to latest snapshot.

* Sun Jul 30 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git170729.222421.9fee6cdc-1
- Update to latest snapshot.

* Mon Jul 24 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git170723.000103.b837f72d-1
- Update to version 0.4.3.

* Mon Jul 24 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git170723.000103.b837f72d-1
- Update to latest snapshot.

* Wed Jul 12 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git170712.163835.11c48a95-1
- Update to latest snapshot.

* Wed Jul 12 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git170712.045915.f3ecbc73-1
- Update to latest snapshot.

* Fri Jul 07 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git170707.040916.a72626a3-1
- Update to latest snapshot.

* Sun Jul 02 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git170702.190626.3a3c273c-1
- Update to latest snapshot.

* Sun Jul 02 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git170702.185458.d9f8601c-1
- Update to latest snapshot.

* Tue Jun 27 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git170627.083411.7b3f8023-1
- Update to latest snapshot.

* Wed Jun 21 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git170621.162040.0060bb0b-1
- Update to latest snapshot.

* Tue Jun 20 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git170620.085516.85c0a653-1
- Update to latest snapshot.

* Mon Jun 19 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git170619.110718.9368f985-1
- Update to latest snapshot.

* Sat Jun 17 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git170616.232032.4578d7a8-1
- Update to latest snapshot.

* Wed Jun 14 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git170614.160700.fd133cd6-1
- Update to latest snapshot.

* Fri Jun 02 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git170601.231200.d471bee3-1
- Update to latest snapshot.

* Thu Jun 01 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git170601.214217.1d034cba-1
- Update to latest snapshot.

* Wed May 31 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git170531.170754.69bca1b3-1
- Update to latest snapshot.

* Tue May 16 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git170516.184717.12d615e4-1
- Update to latest snapshot.

* Mon May 15 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.2+git170515.121953.b227901c-1
- Update to version 0.4.2.

* Mon May 15 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.1+git170515.121953.b227901c-1
- Update to latest snapshot.

* Thu May 11 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.1+git170511.085026.ef26cbe1-1
- Update to latest snapshot.

* Wed May 10 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.1+git170510.112639.04d5c037-2
- Adapt to upstream licensing fixes.

* Wed May 10 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.1+git170510.112639.04d5c037-1
- Update to latest snapshot.

* Tue May 09 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.1+git170509.083853.141565c0-1
- Update to latest snapshot.

* Sun May 07 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.1+git170506.221628.01d1039c-1
- Update to version 0.4.1.

* Sun May 07 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.4+rev961-1
- Update to latest snapshot.

* Sat May 06 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.4+rev959-1
- Update to latest snapshot.

* Sun Apr 30 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.4+rev958-1
- Update to latest snapshot.

* Sat Apr 29 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.4+rev957-1
- Update to latest snapshot.

* Fri Apr 28 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.4+rev956-1
- Update to latest snapshot.

* Fri Apr 28 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.4+rev955-2
- Adapt to upstream file changes.

* Thu Apr 27 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.4+rev955-1
- Update to latest snapshot.

* Thu Apr 20 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.4+rev954-1
- Update to latest snapshot.

* Fri Apr 07 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.4+rev953-1
- Update to latest snapshot.

* Wed Mar 22 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.4+rev952-1
- Update to latest snapshot.

* Mon Mar 20 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.4+rev951-1
- Update to latest snapshot.

* Sun Mar 19 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.4+rev950-1
- Update to version 0.4.0.4.

* Sun Mar 19 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.2+rev950-1
- Update to latest snapshot.

* Sun Mar 19 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.2+rev949-1
- Update to latest snapshot.

* Wed Mar 15 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.2+rev948-1
- Update to latest snapshot.

* Fri Mar 03 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.2+rev947-1
- Update to latest snapshot.

* Thu Mar 02 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.2+rev946-1
- Update to latest snapshot.

* Tue Feb 28 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.2+rev945-1
- Update to latest snapshot.

* Mon Feb 27 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.2+rev944-1
- Update to latest snapshot.

* Mon Feb 20 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.2+rev943-1
- Update to latest snapshot.

* Wed Feb 15 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.2+rev942-1
- Update to latest snapshot.

* Mon Feb 13 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.2+rev941-1
- Update to latest snapshot.

* Sun Feb 12 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.2+rev940-1
- Update to latest snapshot.

* Sat Feb 11 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.2+rev939-1
- Update to latest snapshot.

* Fri Feb 10 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.2+rev938-1
- Update to latest snapshot.

* Wed Feb 08 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.2+rev937-1
- Update to latest snapshot.

* Sat Feb 04 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.2+rev936-1
- Update to latest snapshot.

* Thu Feb 02 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.2+rev935-1
- Update to latest snapshot.

* Mon Jan 30 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.2+rev934-1
- Update to latest snapshot.

* Sun Jan 29 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.2+rev933-1
- Update to latest snapshot.

* Sat Jan 28 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.2+rev932-1
- Update to latest snapshot.

* Mon Jan 23 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.2+rev931-1
- Update to latest snapshot.

* Sun Jan 22 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.2+rev930-1
- Update to latest snapshot.

* Mon Jan 09 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.2+rev929-1
- Update to version 0.4.0.2.

* Sun Jan 08 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.2+rev928-1
- Update to version 0.4.0.2.

* Sat Jan 07 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.2+rev927-1
- Update to version 0.4.0.2.

* Fri Jan 06 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.2+rev926-1
- Update to version 0.4.0.2.

* Wed Jan 04 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.2+rev925-1
- Update to version 0.4.0.2.

* Sat Dec 31 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.2+rev923-1
- Update to latest snapshot.

* Fri Dec 30 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.2+rev922-1
- Update to latest snapshot.

* Thu Dec 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.2+rev921-1
- Update to latest snapshot.

* Wed Dec 28 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.2+rev920-1
- Update to latest snapshot.

* Tue Dec 20 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.2+rev919-1
- Update to latest snapshot.

* Mon Dec 19 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.2+rev918-1
- Update to latest snapshot.

* Mon Dec 12 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.2+rev917-1
- Update to latest snapshot.

* Sun Dec 04 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.2+rev916-1
- Update to latest snapshot.

* Fri Dec 02 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.2+rev915-1
- Update to latest snapshot.

* Sat Nov 19 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.2+rev914-1
- Update to latest snapshot.

* Tue Nov 01 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.2+rev913-1
- Update to latest snapshot.

* Mon Oct 31 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.2+rev912-1
- Update to version 0.4.0.2.

* Mon Oct 31 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.1+rev912-1
- Update to latest snapshot.

* Mon Oct 31 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.1+rev911-1
- Update to version 0.4.0.1.

* Sat Oct 22 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4+rev910-1
- Update to latest snapshot.

* Fri Oct 21 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4+rev909-1
- Update to latest snapshot.

* Thu Oct 20 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4+rev908-1
- Update to latest snapshot.

* Tue Oct 18 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4+rev907-1
- Update to latest snapshot.

* Mon Oct 17 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4+rev906-1
- Update to latest snapshot.

* Thu Oct 13 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4+rev905-2
- Ignore appdata verification result.

* Tue Oct 11 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4+rev905-1
- Update to latest snapshot.

* Mon Oct 10 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4+rev904-1
- Update to latest snapshot.

* Sat Oct 01 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4+rev903-1
- Update to latest snapshot.

* Thu Sep 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4+rev902-2
- Spec file cleanups.

* Tue Sep 27 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4+rev902-1
- Update to latest snapshot.

* Sat Sep 24 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4+rev901-1
- Update to latest snapshot.

* Thu Sep 22 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4+rev900-1
- Update to version 0.4.

* Tue Sep 20 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev899-1
- Update to latest snapshot.

* Wed Sep 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev898-1
- Update to latest snapshot.

* Tue Sep 13 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev897-1
- Update to latest snapshot.

* Mon Sep 12 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev896-1
- Update to latest snapshot.

* Sun Sep 11 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev895-1
- Update to latest snapshot.

* Sat Sep 10 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev894-1
- Update to latest snapshot.

* Sun Sep 04 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev893-1
- Update to latest snapshot.

* Fri Sep 02 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev892-1
- Update to latest snapshot.

* Wed Aug 31 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev891-1
- Update to latest snapshot.

* Sat Aug 27 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev890-1
- Update to latest snapshot.

* Fri Aug 26 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev889-2
- Update for packaging changes.

* Fri Aug 26 2016 Fabio Valentini <decathorpe@gmail.com>
- Ignore .desktop file validation results (translators break this frequently).

* Fri Aug 26 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev889-1
- Update to latest snapshot.

* Tue Aug 16 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev888-1
- Update to latest snapshot.

* Mon Aug 15 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev887-1
- Update to latest snapshot.

* Sun Aug 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev886-1
- Update to latest snapshot.

* Thu Aug 11 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev885-1
- Update to latest snapshot.

* Wed Aug 10 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev884-1
- Update to latest snapshot.

* Wed Aug 10 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev883-1
- Update to latest snapshot.

* Tue Aug 09 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev882-1
- Update to latest snapshot.

* Sun Aug 07 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev881-2
- Update for packaging changes.

* Sun Aug 07 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev881-1
- Update to latest snapshot.

* Sat Aug 06 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev880-1
- Update to latest snapshot.

* Fri Aug 05 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev879-2
- Update for packaging changes.

* Fri Aug 05 2016 Fabio Valentini <decathorpe@gmail.com>
- Add BR: intltool to fix build.

* Fri Aug 05 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev879-1
- Update to latest snapshot.

* Thu Aug 04 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev878-1
- Update to latest snapshot.

* Tue Aug 02 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev872-1
- Update to latest snapshot.

* Fri Jul 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev871-1
- Update to latest snapshot.

* Fri Jul 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev870-1
- Update to latest snapshot.

* Thu Jul 28 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev869-1
- Update to latest snapshot.

* Wed Jul 27 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev868-1
- Update to latest snapshot.

* Tue Jul 26 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev867-1
- Update to latest snapshot.

* Mon Jul 25 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev866-1
- Update to latest snapshot.

* Mon Jul 18 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev865-1
- Update to latest snapshot.

* Mon Jul 11 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev862-2
- Update for packaging changes.

* Sun Jul 10 2016 Fabio Valentini <decathorpe@gmail.com>
- Adapt to desktop file name change.

* Sun Jul 10 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev862-1
- Update to latest snapshot.

* Fri Jul 08 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev861-1
- Update to latest snapshot.

* Thu Jul 07 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev860-1
- Update to latest snapshot.

* Wed Jul 06 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev859-1
- Update to latest snapshot.

* Wed Jul 06 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev858-2
- Update for packaging changes.

* Tue Jun 21 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev853-1
- Update to latest snapshot.

* Mon Jun 20 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev852-1
- Update to latest snapshot.

* Mon Jun 20 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev851-1
- Update to latest snapshot.

* Sat Jun 18 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev850-1
- Update to latest snapshot.

* Fri Jun 17 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev849-1
- Update to latest snapshot.

* Tue Jun 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev848-1
- Update to latest snapshot.

* Sun Jun 12 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev847-1
- Update to latest snapshot.

* Sat Jun 11 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev846-1
- Update to latest snapshot.

* Sat Jun 11 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev845-1
- Update to latest snapshot.

* Fri Jun 03 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev844-1
- Update to latest snapshot.

* Tue May 31 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev843-1
- Update to latest snapshot.

* Mon May 30 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev842-3
- Update for packaging changes.

* Sun May 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev842-2
- Update for packaging changes.

* Thu May 26 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev842-1
- Update to latest snapshot.

* Thu May 26 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev841-1
- Update to latest snapshot.

* Wed May 25 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev840-1
- Update to latest snapshot.

* Fri May 20 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev839-1
- Update to latest snapshot.

* Wed May 04 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev838-1
- Update to latest snapshot.

* Sun May 01 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev838-1
- Update to new upstream snapshot.

* Sat Apr 30 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev837-1
- Update to new upstream snapshot.

* Sat Apr 23 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev836-1
- Update to new upstream snapshot.

* Mon Apr 18 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev835-1
- Update to new upstream snapshot.

* Sun Apr 17 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev834-1
- Update to new upstream snapshot.

* Sun Apr 10 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev833-1
- Update to new upstream snapshot.

* Sat Apr 09 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev832-1
- Update to new upstream snapshot.

* Tue Mar 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev831-1
- Update to new upstream snapshot.

* Fri Mar 25 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev829-1
- Update to new upstream snapshot.

* Thu Mar 24 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev828-1
- Update to new upstream snapshot.

* Mon Mar 21 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev827-1
- Update to new upstream snapshot.

* Sun Mar 13 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev824-1
- Update to new upstream snapshot.

* Tue Mar 08 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev823-1
- Update to new upstream snapshot.

* Mon Mar 07 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev822-1
- Update to new upstream snapshot.

* Sat Mar 05 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev820-1
- Update to new upstream snapshot.

* Fri Mar 04 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev819-1
- Update to new upstream snapshot.

* Thu Mar 03 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev818-1
- Update to new upstream snapshot.

* Fri Feb 26 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev815-1
- Update to new upstream snapshot.

* Thu Feb 18 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4~rev812-1
- Update to new upstream snapshot.

* Tue Feb 02 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.3~rev811-1
- Update to new upstream snapshot.

* Mon Feb 01 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.3~rev810-1
- Update to new upstream snapshot.

* Fri Jan 22 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.3~rev809-1
- Update to new upstream snapshot.

* Thu Jan 21 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.3~rev808-1
- Update to new upstream snapshot.

* Sat Jan 16 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.3~rev807-1
- Update to new upstream snapshot.

* Wed Jan 13 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.3~rev806-1
- Update to new upstream snapshot.

* Mon Jan 11 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.3~rev805-1
- Update to new upstream snapshot.

* Sun Jan 03 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.3~rev803-1
- Update to new upstream snapshot.

* Fri Jan 01 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.3~rev802-1
- Update to new upstream snapshot.

* Thu Dec 31 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.3~rev801-1
- Update to new upstream snapshot.

* Mon Dec 28 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.3~rev800-1
- Update to new upstream snapshot.

* Sun Dec 27 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.3~rev799-1
- Update to new upstream snapshot.

* Wed Dec 16 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.3~rev798-1
- Update to new upstream snapshot.

* Tue Dec 15 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.3~rev797-1
- Update to new upstream snapshot.

* Mon Dec 14 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.3~rev796-1
- Update to new upstream snapshot.

* Sun Dec 13 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.3~rev795-1
- Update to new upstream snapshot.

* Sun Dec 13 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.3~rev794-2
- Add appdata file and check to spec.

* Sat Dec 12 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.3~rev794-1
- Update to new upstream snapshot.

* Fri Dec 11 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.3~rev792-1
- Update to new upstream snapshot.

* Wed Dec 09 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.3~rev790-1
- Update to new upstream snapshot.

* Tue Dec 08 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.3~rev789-1
- Update to new upstream snapshot.

* Sun Dec 06 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.3~rev788-1
- Update to new upstream snapshot.

* Thu Dec 03 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.3~rev781-1
- Update to new upstream snapshot.

* Wed Dec 02 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.3~rev780-1
- Update to new upstream snapshot.

* Tue Dec 01 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.3~rev779-1
- Update to new upstream snapshot.

* Mon Nov 30 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.3~rev778-1
- Update to new upstream snapshot.

* Sun Nov 29 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.3~rev777-1
- Update to new upstream snapshot.

* Sat Nov 28 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.3~rev776-1
- Update to new upstream snapshot.

* Fri Nov 27 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.3~rev774-1
- Update to new upstream snapshot.

* Thu Nov 26 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.3~rev772-1
- Update to new upstream snapshot.

* Tue Nov 24 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.3~rev771-1
- Update to new upstream snapshot.

* Sun Nov 15 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.3~rev769-1
- Update to new upstream snapshot.

* Sat Nov 14 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.3~rev768-1
- Update to new upstream snapshot.

* Fri Nov 13 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.3~rev767-1
- Update to new upstream snapshot.

* Mon Nov 09 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.3~rev766-1
- Update to new upstream snapshot.

* Fri Oct 23 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.3~rev765-1
- Update to new upstream snapshot.

* Wed Oct 21 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.3~rev764-1
- Update to new upstream snapshot.

* Mon Oct 19 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.3~rev763-1
- Update to new upstream snapshot.

* Sun Oct 18 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.3~rev762-1
- Update to new upstream snapshot.

* Wed Oct 14 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.3~rev761-1
- Update to new upstream snapshot.

* Thu Oct 08 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.3~rev760-1
- Update to new upstream snapshot.

* Sat Oct 03 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.3~rev758-1
- Update to new upstream snapshot.

* Fri Oct 02 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.3~rev757-1
- Update to new upstream snapshot.

* Tue Sep 29 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.3~rev756-1
- Update to new upstream snapshot.

* Sun Sep 27 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.3~rev755-1
- Update to new upstream snapshot.

* Fri Sep 25 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.3~rev754-3
- Try to fix f23-x64 build.

* Tue Sep 22 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.3~rev754-2
- Change BR:vte-2.90 to BR:vte-291.

* Mon Sep 21 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.3~rev754-1
- Update to new upstream snapshot.

* Sun Sep 06 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.3~rev752-1
- Update to new upstream snapshot.

* Fri Sep 04 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.3~rev751-2
- rebuild trigger for granite soname bump

* Thu Sep 03 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.3~rev751-1
- Update to new upstream snapshot.

* Tue Sep 01 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.3~rev750-1
- Update to new upstream snapshot.

* Thu Aug 20 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.3~rev749-1
- Update to new upstream snapshot.

* Wed Aug 19 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1.3~rev748-1
- Initial package.


