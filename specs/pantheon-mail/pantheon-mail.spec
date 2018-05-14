Name:           pantheon-mail
Summary:        E-Mail client for Pantheon
Version:        1.0.6+git%{date}.%{commit}
Release:        1%{?dist}
License:        LGPLv2+

URL:            https://github.com/elementary/mail
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  vala >= 0.22.1

BuildRequires:  pkgconfig(gcr-3) >= 3.10.1
BuildRequires:  pkgconfig(gee-0.8) >= 0.8.5
BuildRequires:  pkgconfig(glib-2.0) >= 2.40
BuildRequires:  pkgconfig(gmime-2.6) >= 2.6.17
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.12.0
BuildRequires:  pkgconfig(libaccounts-glib)
BuildRequires:  pkgconfig(libgsignon-glib)
BuildRequires:  pkgconfig(libcanberra) >= 0.28
BuildRequires:  pkgconfig(libsecret-1) >= 0.11
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(libxml-2.0) >= 2.7.8
BuildRequires:  pkgconfig(sqlite3) >= 3.7.4
BuildRequires:  pkgconfig(unity) >= 5.12.0
BuildRequires:  pkgconfig(webkitgtk-3.0)


%description
Pantheon Mail is the E-Mail client for the Pantheon desktop.


%package        contract
Summary:        E-Mail client for Pantheon (contractor support)

Requires:       contractor
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    contract
Pantheon Mail is the E-Mail client for the Pantheon desktop.
This package contains the contractor support.


%prep
%autosetup


%build
mkdir build && pushd build
%cmake .. \
    -DICON_UPDATE:BOOL=OFF \
    -DDESKTOP_UPDATE:BOOL=OFF
%make_build
popd


%install
pushd build
%make_install
popd

%find_lang pantheon-mail


%check
desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/org.pantheon.mail.desktop
desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/pantheon-mail-autostart.desktop

appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/org.pantheon.mail.appdata.xml


%files -f pantheon-mail.lang
%doc README.md
%license COPYING

%{_bindir}/pantheon-mail

%{_datadir}/accounts/applications/pantheon-mail.application
%{_datadir}/applications/org.pantheon.mail.desktop
%{_datadir}/applications/pantheon-mail-autostart.desktop
%{_datadir}/glib-2.0/schemas/org.pantheon.mail.gschema.xml
%{_datadir}/metainfo/org.pantheon.mail.appdata.xml


%files contract
%{_bindir}/mail-attach
%{_datadir}/contractor/mail-attach.contract


%changelog
* Mon May 14 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.6+git180514.000214.6f805c22-1
- Update to latest snapshot.

* Fri May 11 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.6+git180511.104149.cb731432-1
- Update to latest snapshot.

* Mon May 07 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.6+git180507.000242.4e8f7e8c-1
- Update to latest snapshot.

* Sun May 06 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.6+git180504.000555.568d0369-1
- Update to latest snapshot.

* Thu May 03 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.6+git180503.090246.38ffe6e9-1
- Update to latest snapshot.

* Tue May 01 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.6+git180427.000251.562be783-1
- Update to latest snapshot.

* Tue Apr 24 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.6+git180424.000716.e378af16-1
- Update to latest snapshot.

* Mon Apr 23 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.6+git180423.111055.ae7b509c-1
- Update to latest snapshot.

* Fri Apr 20 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.6+git180420.001143.10768a9c-1
- Update to latest snapshot.

* Thu Apr 19 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.6+git180419.174804.7bb79b51-1
- Update to latest snapshot.

* Fri Apr 13 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.6+git180413.181903.06f10f30-1
- Update to latest snapshot.

* Sun Apr 08 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.6+git180407.000856.7b59981b-1
- Update to latest snapshot.

* Thu Apr 05 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.6+git180405.190042.4ec7c008-1
- Update to latest snapshot.

* Tue Apr 03 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.6+git180402.000444.4aa0457c-1
- Update to latest snapshot.

* Tue Mar 27 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.6+git180327.000207.f884ed28-1
- Update to latest snapshot.

* Thu Mar 22 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.6+git180322.000527.dc6f56d0-1
- Update to latest snapshot.

* Tue Mar 20 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.6+git180320.001130.ebbc1531-1
- Update to latest snapshot.

* Wed Mar 07 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.6+git180307.000946.b55c549c-1
- Update to latest snapshot.

* Wed Feb 21 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.6+git180221.000742.a6e2a157-1
- Update to latest snapshot.

* Sun Feb 18 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.6+git180218.110917.18522f56-1
- Update to latest snapshot.

* Sat Feb 17 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.6+git180217.204609.831e2a32-1
- Update to latest snapshot.

* Mon Feb 12 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.6+git180212.000422.3b2f0c2a-1
- Update to latest snapshot.

* Wed Feb 07 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.6+git180207.173722.5cb78a1c-1
- Update to latest snapshot.

* Wed Jan 31 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.6+git180131.000929.38e94894-1
- Update to latest snapshot.

* Mon Jan 29 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.6+git180129.000221.07b15c0d-1
- Update to latest snapshot.

* Sun Jan 28 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.6+git180128.000810.007dd58b-1
- Update to latest snapshot.

* Mon Jan 22 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.6+git180122.182500.5c25872c-1
- Update to latest snapshot.

* Sat Nov 04 2017 Fabio Valentini <decathorpe@gmail.com> - 1.0.6+git171104.071344.e5f99c3e-1
- Update to latest snapshot.

* Mon Sep 25 2017 Fabio Valentini <decathorpe@gmail.com> - 1.0.6+git170925.140534.21faa31d-1
- Update to latest snapshot.

* Thu Aug 24 2017 Fabio Valentini <decathorpe@gmail.com> - 1.0.6+git170824.063322.9e5a3156-1
- Update to version 1.0.6.

* Thu Aug 24 2017 Fabio Valentini <decathorpe@gmail.com> - 1.0.5+git170824.063322.9e5a3156-1
- Update to latest snapshot.

* Thu Jul 20 2017 Fabio Valentini <decathorpe@gmail.com> - 1.0.5+git170720.180807.5ff1e19b-1
- Update to latest snapshot.

* Sat Jul 08 2017 Fabio Valentini <decathorpe@gmail.com> - 1.0.5+git170708.055003.6d5da182-1
- Update to latest snapshot.

* Sat Jul 01 2017 Fabio Valentini <decathorpe@gmail.com> - 1.0.5+git170701.172125.becd8fa7-1
- Update to latest snapshot.

* Sat Jul 01 2017 Fabio Valentini <decathorpe@gmail.com> - 1.0.5+git170630.014106.62b9c645-1
- Update to latest snapshot.

* Sun Jun 18 2017 Fabio Valentini <decathorpe@gmail.com> - 1.0.5+git170617.161241.d9d06237-1
- Update to latest snapshot.

* Wed Jun 14 2017 Fabio Valentini <decathorpe@gmail.com> - 1.0.5+git170614.153814.facd70f9-1
- Update to latest snapshot.

* Sun May 28 2017 Fabio Valentini <decathorpe@gmail.com> - 1.0.5+git170527.211033.c25cf6f2-1
- Update to latest snapshot.

* Sat May 27 2017 Fabio Valentini <decathorpe@gmail.com> - 1.0.5+git170527.140806.df4fccf1-1
- Update to latest snapshot.

* Thu May 25 2017 Fabio Valentini <decathorpe@gmail.com> - 1.0.5+git170524.230052.b898462b-1
- Update to latest snapshot.

* Sun May 14 2017 Fabio Valentini <decathorpe@gmail.com> - 1.0.5+git170514.144333.1963d273-1
- Update to latest snapshot.

* Wed May 10 2017 Fabio Valentini <decathorpe@gmail.com> - 1.0.5+git170510.112743.14b3f508-1
- Update to latest snapshot.

* Tue May 09 2017 Fabio Valentini <decathorpe@gmail.com> - 1.0.5+git170509.102029.88ea896c-1
- Update to latest snapshot.

* Mon May 08 2017 Fabio Valentini <decathorpe@gmail.com> - 1.0.5+git170508.153122.5a537d7e-1
- Update to latest snapshot.

* Sun Apr 30 2017 Fabio Valentini <decathorpe@gmail.com> - 1.0.5+git170428.101350.e1bb88dc-1
- Update to latest snapshot.

* Wed Apr 26 2017 Fabio Valentini <decathorpe@gmail.com> - 1.0.5+git170410.105449.585ae7b1-1
- Update to latest snapshot.

* Tue Apr 18 2017 Fabio Valentini <decathorpe@gmail.com> - 1.0.5-1
- Initial package.

