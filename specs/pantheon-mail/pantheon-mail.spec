Name:           pantheon-mail
Summary:        E-Mail client for Pantheon
Version:        1.0.5+git%{date}.%{commit}
Release:        1%{?dist}
License:        LGPLv2+

URL:            https://launchpad.net/pantheon-mail
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  vala >= 0.22.1

BuildRequires:  pkgconfig(gcr-3) >= 3.10.1
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(glib-2.0) >= 2.40
BuildRequires:  pkgconfig(gmime-2.6) >= 2.6.17
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.10.0
BuildRequires:  pkgconfig(libaccounts-glib)
BuildRequires:  pkgconfig(libgsignon-glib)
BuildRequires:  pkgconfig(libcanberra) >= 0.28
BuildRequires:  pkgconfig(libsecret-1) >= 0.11
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(libxml-2.0) >= 2.7.8
BuildRequires:  pkgconfig(sqlite3) >= 3.7.4
BuildRequires:  pkgconfig(unity) >= 5.12.0
BuildRequires:  pkgconfig(webkitgtk-3.0)

Requires:       contractor



%description
Pantheon Mail is the E-Mail client for the Pantheon desktop.


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

# move appdata to "correct" location
mv %{buildroot}/%{_datadir}/metainfo %{buildroot}/%{_datadir}/appdata


%check
desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/org.pantheon.mail.desktop
desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/pantheon-mail-autostart.desktop

appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/appdata/org.pantheon.mail.appdata.xml


%files -f pantheon-mail.lang
%license COPYING

%{_bindir}/pantheon-mail
%{_bindir}/mail-attach

%{_datadir}/accounts/applications/pantheon-mail.application
%{_datadir}/appdata/org.pantheon.mail.appdata.xml
%{_datadir}/applications/org.pantheon.mail.desktop
%{_datadir}/applications/pantheon-mail-autostart.desktop
%{_datadir}/contractor/mail-attach.contract
%{_datadir}/glib-2.0/schemas/org.pantheon.mail.gschema.xml


%changelog
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

