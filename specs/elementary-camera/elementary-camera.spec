Name:           elementary-camera
Summary:        Fast and beautiful camera app
Version:        0.3.0.1+git%{date}.%{commit}
Release:        2%{?dist}
License:        GPLv3
URL:            https://github.com/elementary/camera

Source0:        %{name}-%{version}.tar.gz
Source1:        %{name}.conf

BuildRequires:  appstream
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  vala >= 0.24
BuildRequires:  vala-tools

BuildRequires:  pkgconfig(clutter-gst-3.0)
BuildRequires:  pkgconfig(clutter-gtk-1.0)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libcanberra)

Provides:       snap-photobooth
Obsoletes:      snap-photobooth


%description
A fast and beautiful camera app.


%prep
%autosetup


%build
%meson
%meson_build


%install
%meson_install
%find_lang pantheon-camera


%check
desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/*.desktop

appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/*.appdata.xml


%files -f pantheon-camera.lang
%{_bindir}/pantheon-camera

%{_datadir}/applications/org.pantheon.camera.desktop
%{_datadir}/glib-2.0/schemas/org.pantheon.camera.gschema.xml
%{_datadir}/metainfo/org.pantheon.camera.appdata.xml


%changelog
* Wed Oct 11 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git171010.092010.3494a051-2
- Adapt to upstream file changes.

* Tue Oct 10 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git171010.092010.3494a051-1
- Update to latest snapshot.

* Mon Sep 25 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git170925.094829.b4e015e7-1
- Update to latest snapshot.

* Tue Sep 19 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git170704.192116.7bb3dae9-1
- Update to version 0.3.0.1.


