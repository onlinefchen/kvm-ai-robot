# KVMARM 邮件列表 AI 总结报告

**生成时间**: 2025-10-22 09:59:56

**分析周期**: 最近 7 天

## 📊 总体统计

- **总邮件数**: 154
- **总 Thread 数**: 27
- **大型 Thread** (>20封): 1 个

### 分类分布

- **PATCH**: 23 threads (140 邮件)
- **GIT PULL**: 1 threads (1 邮件)
- **Other**: 3 threads (13 邮件)

---

## 📌 PATCH

共 23 个 thread

---

### Thread 1: [PATCH v9 0/6] KVM: arm64: Map GPU device memory as cacheable

**📧 邮件数**: 31 | **👥 参与者**: 6 | **📅 开始时间**: Sat, 21 Jun 2025 04:21:05 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于在 KVM（内核虚拟机）中将 GPU 设备内存映射为可缓存的补丁系列（PATCH v9 0/6）。该补丁旨在解决 Grace Hopper 和 Blackwell 超级芯片等平台上 CPU 可访问的缓存一致性 GPU 内存的映射问题。

在历史讨论中，Ankit Agrawal 提出了多个补丁，主要包括：
1. 将设备变量重命名为更具描述性的名称，以便更好地反映其功能。
2. 更新检测设备内存的检查逻辑，确保 KVM 能够正确使用缓存维护操作。
3. 阻止缓存 PFNMAP 映射，以修复由于 S1 和 S2 映射属性不匹配而导致的安全漏洞。
4. 引入新的功能以确定硬件缓存管理支持。

本周的新讨论中，Ankit 提醒参与者对补丁进行审查，并报告了在 qemu-kvm 下成功将 GPU 分配给虚拟机的测试结果，之前的 nvidia-smi 命令在未应用补丁时会失败。Jason Gunthorpe 和 David Hildenbrand 对补丁进行了审查，提出了一些建议和修改意见，特别是关于缓存映射的逻辑和条件的简化。

总体而言，补丁系列得到了积极的反馈，参与者一致认为其方向正确，并在讨论中提出了对未来版本的改进建议。

#### 📝 邮件列表

1. **[06-21 04:21]** [PATCH v9 0/6] KVM: arm64: Map GPU device memory as cacheable
   - 发件人: ankita <ankita@nvidia.com>
2. **[06-21 04:21]** [PATCH v9 1/6] KVM: arm64: Rename the device variable to s2_force_noncacheable
   - 发件人: ankita <ankita@nvidia.com>
3. **[06-21 04:21]** [PATCH v9 2/6] KVM: arm64: Update the check to detect device memory
   - 发件人: ankita <ankita@nvidia.com>
4. **[06-21 04:21]** [PATCH v9 3/6] KVM: arm64: Block cacheable PFNMAP mapping
   - 发件人: ankita <ankita@nvidia.com>
5. **[06-21 04:21]** [PATCH v9 4/6] KVM: arm64: New function to determine hardware cache management support
   - 发件人: ankita <ankita@nvidia.com>
6. **[06-21 04:21]** [PATCH v9 5/6] KVM: arm64: Allow cacheable stage 2 mapping using VMA flags
   - 发件人: ankita <ankita@nvidia.com>
7. **[06-21 04:21]** [PATCH v9 6/6] KVM: arm64: Expose new KVM cap for cacheable PFNMAP
   - 发件人: ankita <ankita@nvidia.com>
8. **[06-27 14:49]** Re: [PATCH v9 3/6] KVM: arm64: Block cacheable PFNMAP mapping
   - 发件人: Will Deacon <will@kernel.org>
9. **[06-30 01:56]** Re: [PATCH v9 3/6] KVM: arm64: Block cacheable PFNMAP mapping
   - 发件人: Ankit Agrawal <ankita@nvidia.com>
10. **[06-30 09:25]** Re: [PATCH v9 3/6] KVM: arm64: Block cacheable PFNMAP mapping
   - 发件人: Jason Gunthorpe <jgg@nvidia.com>
11. **[07-02 09:33]** Re: [PATCH v9 0/6] KVM: arm64: Map GPU device memory as cacheable
   - 发件人: Ankit Agrawal <ankita@nvidia.com>
12. **[07-02 12:51]** Re: [PATCH v9 0/6] KVM: arm64: Map GPU device memory as cacheable
   - 发件人: Donald Dutile <ddutile@redhat.com>
13. **[07-04 14:21]** Re: [PATCH v9 3/6] KVM: arm64: Block cacheable PFNMAP mapping
   - 发件人: David Hildenbrand <david@redhat.com>
14. **[07-04 10:41]** Re: [PATCH v9 1/6] KVM: arm64: Rename the device variable to
 s2_force_noncacheable
   - 发件人: Jason Gunthorpe <jgg@nvidia.com>
15. **[07-04 10:43]** Re: [PATCH v9 2/6] KVM: arm64: Update the check to detect device
 memory
   - 发件人: Jason Gunthorpe <jgg@nvidia.com>
16. **[07-04 10:44]** Re: [PATCH v9 6/6] KVM: arm64: Expose new KVM cap for cacheable
 PFNMAP
   - 发件人: Jason Gunthorpe <jgg@nvidia.com>
17. **[07-04 10:45]** Re: [PATCH v9 3/6] KVM: arm64: Block cacheable PFNMAP mapping
   - 发件人: Jason Gunthorpe <jgg@nvidia.com>
18. **[07-04 10:47]** Re: [PATCH v9 4/6] KVM: arm64: New function to determine hardware
 cache management support
   - 发件人: Jason Gunthorpe <jgg@nvidia.com>
19. **[07-04 15:57]** Re: [PATCH v9 1/6] KVM: arm64: Rename the device variable to
 s2_force_noncacheable
   - 发件人: David Hildenbrand <david@redhat.com>
20. **[07-04 16:02]** Re: [PATCH v9 2/6] KVM: arm64: Update the check to detect device
 memory
   - 发件人: David Hildenbrand <david@redhat.com>
21. **[07-04 11:04]** Re: [PATCH v9 5/6] KVM: arm64: Allow cacheable stage 2 mapping using
 VMA flags
   - 发件人: Jason Gunthorpe <jgg@nvidia.com>
22. **[07-04 16:09]** Re: [PATCH v9 3/6] KVM: arm64: Block cacheable PFNMAP mapping
   - 发件人: David Hildenbrand <david@redhat.com>
23. **[07-04 16:10]** Re: [PATCH v9 4/6] KVM: arm64: New function to determine hardware
 cache management support
   - 发件人: David Hildenbrand <david@redhat.com>
24. **[07-04 16:13]** Re: [PATCH v9 5/6] KVM: arm64: Allow cacheable stage 2 mapping using
 VMA flags
   - 发件人: David Hildenbrand <david@redhat.com>
25. **[07-04 16:15]** Re: [PATCH v9 6/6] KVM: arm64: Expose new KVM cap for cacheable
 PFNMAP
   - 发件人: David Hildenbrand <david@redhat.com>
26. **[07-04 12:04]** Re: [PATCH v9 6/6] KVM: arm64: Expose new KVM cap for cacheable
 PFNMAP
   - 发件人: Jason Gunthorpe <jgg@nvidia.com>
27. **[07-04 17:04]** Re: [PATCH v9 3/6] KVM: arm64: Block cacheable PFNMAP mapping
   - 发件人: Will Deacon <will@kernel.org>
28. **[07-04 16:20]** Re: [PATCH v9 6/6] KVM: arm64: Expose new KVM cap for cacheable
 PFNMAP
   - 发件人: Ankit Agrawal <ankita@nvidia.com>
29. **[07-04 13:47]** Re: [PATCH v9 3/6] KVM: arm64: Block cacheable PFNMAP mapping
   - 发件人: Jason Gunthorpe <jgg@nvidia.com>
30. **[07-04 16:51]** Re: [PATCH v9 5/6] KVM: arm64: Allow cacheable stage 2 mapping using
 VMA flags
   - 发件人: Ankit Agrawal <ankita@nvidia.com>
31. **[07-04 13:56]** Re: [PATCH v9 6/6] KVM: arm64: Expose new KVM cap for cacheable
 PFNMAP
   - 发件人: Jason Gunthorpe <jgg@nvidia.com>

---

### Thread 2: [PATCH v9 00/43] arm64: Support for Arm CCA in KVM

**📧 邮件数**: 13 | **👥 参与者**: 3 | **📅 开始时间**: Wed, 25 Jun 2025 01:51:53 +0000

#### 🤖 AI 总结

本邮件线程讨论的是针对 ARM64 架构的 KVM（内核虚拟机）支持 Arm CCA（Cache Coherent Accelerator）的一系列补丁（PATCH v9 00/43）。历史讨论中，Emi Kisanuki 提到在 Fujitsu 的内部模拟器上测试了该补丁，结果符合预期，成功启动了虚拟机并通过了大部分 kvm-unit-tests 测试。

本周的新讨论主要集中在对补丁的审查和细节修改上。Gavin Shan 对多个补丁进行了审核，并提出了一些小的修改建议，例如在补丁中明确设置虚拟机状态、改善描述的清晰度等。他还确认了补丁在 QEMU 环境下的测试结果，表示该系列补丁在启动、销毁虚拟机及运行简单工作负载方面表现良好。

总体来看，本周的讨论主要是对补丁的细节审查和确认测试结果，参与者积极提供反馈，推动补丁的完善和最终合并。

#### 📝 邮件列表

1. **[06-25 01:51]** RE: [PATCH v9 00/43] arm64: Support for Arm CCA in KVM
   - 发件人: Emi Kisanuki (Fujitsu) <fj0570is@fujitsu.com>
2. **[07-01 16:29]** Re: [PATCH v9 06/43] arm64: RME: Define the user ABI
   - 发件人: Gavin Shan <gshan@redhat.com>
3. **[07-01 16:38]** Re: [PATCH v9 09/43] KVM: arm64: Allow passing machine type in KVM
 creation
   - 发件人: Gavin Shan <gshan@redhat.com>
4. **[07-01 16:41]** Re: [PATCH v9 13/43] arm64: RME: Support for the VGIC in realms
   - 发件人: Gavin Shan <gshan@redhat.com>
5. **[07-01 16:42]** Re: [PATCH v9 14/43] KVM: arm64: Support timers in realm RECs
   - 发件人: Gavin Shan <gshan@redhat.com>
6. **[07-01 11:16]** Re: [PATCH v9 12/43] KVM: arm64: vgic: Provide helper for number of
 list registers
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
7. **[07-01 11:20]** Re: [PATCH v9 13/43] arm64: RME: Support for the VGIC in realms
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
8. **[07-02 10:37]** Re: [PATCH v9 15/43] arm64: RME: Allow VMM to set RIPAS
   - 发件人: Gavin Shan <gshan@redhat.com>
9. **[07-02 10:41]** Re: [PATCH v9 16/43] arm64: RME: Handle realm enter/exit
   - 发件人: Gavin Shan <gshan@redhat.com>
10. **[07-02 10:44]** Re: [PATCH v9 17/43] arm64: RME: Handle RMI_EXIT_RIPAS_CHANGE
   - 发件人: Gavin Shan <gshan@redhat.com>
11. **[07-02 11:04]** Re: [PATCH v9 20/43] arm64: RME: Runtime faulting of memory
   - 发件人: Gavin Shan <gshan@redhat.com>
12. **[07-03 14:22]** Re: [PATCH v9 13/43] arm64: RME: Support for the VGIC in realms
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
13. **[07-04 14:58]** Re: [PATCH v9 00/43] arm64: Support for Arm CCA in KVM
   - 发件人: Gavin Shan <gshan@redhat.com>

---

### Thread 3: [PATCH v8 00/14] arm: rework id register storage

**📧 邮件数**: 9 | **👥 参与者**: 2 | **📅 开始时间**: Tue, 17 Jun 2025 17:39:17 +0200

#### 🤖 AI 总结

本邮件线程讨论的主题是对 ARM 架构中 ID 寄存器存储的重构，主要涉及到一系列补丁（PATCH v8 00/14）。历史讨论中，Cornelia Huck 提出了对之前补丁的改进，解决了 Peter 的反馈，确保每个中间阶段都能编译，并增强了脚本的健壮性，以便只抓取所需的寄存器。补丁 13/14 则涉及生成的 cpu-sysregs.h.inc 文件，并得到了多位开发者的审核和签名。

在本周的新讨论中，Cornelia Huck 和 Peter Maydell 继续探讨补丁的细节。Cornelia 提到脚本可能会创建一些不必要的数组条目，并对补丁 1-11 和 14 进行了合并，以简化后续的重基。Peter 讨论了某些 ID 寄存器的实现状态，认为将未实现的寄存器列出是合理的，但对如何处理与缓存相关的寄存器表示担忧。两位开发者还讨论了 KVM 中对这些寄存器的支持情况，认为在未来的实现中应考虑这些寄存器的处理。

总体来看，邮件讨论围绕着 ARM ID 寄存器的存储重构，补丁的细节调整，以及 KVM 对相关寄存器支持的未来方向展开，显示出开发者们对代码质量和功能实现的关注。

#### 📝 邮件列表

1. **[06-17 17:39]** [PATCH v8 00/14] arm: rework id register storage
   - 发件人: Cornelia Huck <cohuck@redhat.com>
2. **[06-17 17:39]** [PATCH v8 13/14] arm/cpu: switch to a generated cpu-sysregs.h.inc
   - 发件人: Cornelia Huck <cohuck@redhat.com>
3. **[06-30 12:04]** Re: [PATCH v8 00/14] arm: rework id register storage
   - 发件人: Cornelia Huck <cohuck@redhat.com>
4. **[06-30 16:23]** Re: [PATCH v8 13/14] arm/cpu: switch to a generated cpu-sysregs.h.inc
   - 发件人: Peter Maydell <peter.maydell@linaro.org>
5. **[06-30 16:25]** Re: [PATCH v8 00/14] arm: rework id register storage
   - 发件人: Peter Maydell <peter.maydell@linaro.org>
6. **[06-30 18:02]** Re: [PATCH v8 00/14] arm: rework id register storage
   - 发件人: Cornelia Huck <cohuck@redhat.com>
7. **[07-01 18:06]** Re: [PATCH v8 13/14] arm/cpu: switch to a generated cpu-sysregs.h.inc
   - 发件人: Cornelia Huck <cohuck@redhat.com>
8. **[07-01 17:49]** Re: [PATCH v8 13/14] arm/cpu: switch to a generated cpu-sysregs.h.inc
   - 发件人: Peter Maydell <peter.maydell@linaro.org>
9. **[07-02 11:01]** Re: [PATCH v8 13/14] arm/cpu: switch to a generated cpu-sysregs.h.inc
   - 发件人: Cornelia Huck <cohuck@redhat.com>

---

### Thread 4: [PATCH v12 10/18] KVM: x86/mmu: Handle guest page faults for
 guest_memfd with shared memory

**📧 邮件数**: 9 | **👥 参与者**: 4 | **📅 开始时间**: Tue, 24 Jun 2025 16:40:18 -0700

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（内核虚拟机）中处理共享内存的 guest_memfd 的页面故障的补丁（PATCH v12 10/18）。该补丁旨在改进 KVM 对于共享内存的支持，特别是在处理页面故障时。

在历史讨论中，参与者们探讨了 guest_memfd 的使用场景，包括在同一虚拟机中同时支持和不支持 mmap 的内存槽。Ackerley Tng 提出了对补丁的命名和功能的质疑，认为命名可能会引起混淆，并讨论了用户空间如何使用这些内存槽的复杂性。

本周的新讨论中，Fuad Tabba 和其他参与者继续围绕补丁的命名和功能进行深入探讨。Fuad 强调了需要明确用户空间的需求，并建议将 mmap 功能的实现放在后续版本中，以避免当前补丁的复杂性。Shivank Garg 和 David Hildenbrand 也支持这一观点，认为应优先实现 mmap 功能，并在后续版本中处理更复杂的用例。

总体来看，本周的讨论集中在如何合理地实现和命名补丁功能上，参与者一致认为应尽快提交当前补丁，同时为未来的扩展留出空间。

#### 📝 邮件列表

1. **[06-24 16:40]** Re: [PATCH v12 10/18] KVM: x86/mmu: Handle guest page faults for
 guest_memfd with shared memory
   - 发件人: Ackerley Tng <ackerleytng@google.com>
2. **[06-27 08:01]** Re: [PATCH v12 10/18] KVM: x86/mmu: Handle guest page faults for
 guest_memfd with shared memory
   - 发件人: Ackerley Tng <ackerleytng@google.com>
3. **[06-30 09:07]** Re: [PATCH v12 10/18] KVM: x86/mmu: Handle guest page faults for
 guest_memfd with shared memory
   - 发件人: Fuad Tabba <tabba@google.com>
4. **[06-30 07:44]** Re: [PATCH v12 10/18] KVM: x86/mmu: Handle guest page faults for
 guest_memfd with shared memory
   - 发件人: Ackerley Tng <ackerleytng@google.com>
5. **[06-30 16:08]** Re: [PATCH v12 10/18] KVM: x86/mmu: Handle guest page faults for
 guest_memfd with shared memory
   - 发件人: Fuad Tabba <tabba@google.com>
6. **[07-01 00:56]** Re: [PATCH v12 10/18] KVM: x86/mmu: Handle guest page faults for
 guest_memfd with shared memory
   - 发件人: Shivank Garg <shivankg@amd.com>
7. **[06-30 22:03]** Re: [PATCH v12 10/18] KVM: x86/mmu: Handle guest page faults for
 guest_memfd with shared memory
   - 发件人: David Hildenbrand <david@redhat.com>
8. **[07-01 07:15]** Re: [PATCH v12 10/18] KVM: x86/mmu: Handle guest page faults for
 guest_memfd with shared memory
   - 发件人: Ackerley Tng <ackerleytng@google.com>
9. **[07-01 16:44]** Re: [PATCH v12 10/18] KVM: x86/mmu: Handle guest page faults for
 guest_memfd with shared memory
   - 发件人: David Hildenbrand <david@redhat.com>

---

### Thread 5: [PATCH v10 0/6] KVM: arm64: Map GPU device memory as cacheable

**📧 邮件数**: 7 | **👥 参与者**: 1 | **📅 开始时间**: Sat, 5 Jul 2025 07:17:11 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于KVM（Kernel-based Virtual Machine）在arm64架构下将GPU设备内存映射为可缓存的补丁（PATCH v10 0/6）。该补丁旨在解决当前KVM对设备内存的限制，使得未添加到内核的设备内存也能被标记为可缓存。

在历史讨论中，参与者们探讨了KVM如何处理不同类型的内存映射，尤其是设备内存与普通内存的区别。现有的KVM代码强制将内存映射为NORMAL或DEVICE_nGnRE，限制了设备内存的缓存能力。补丁通过检查VMA（虚拟内存区域）的pgprot值来判断缓存能力，从而允许安全的缓存映射。

本周的新讨论中，Ankit Agrawal提交了六个补丁，主要包括：
1. 重命名设备变量以更清晰地表达其功能。
2. 更新检测设备内存的逻辑。
3. 阻止缓存PFNMAP映射，以解决安全漏洞。
4. 引入新函数以确定硬件缓存管理支持。
5. 允许基于VMA标志进行可缓存的二级映射。
6. 暴露新的KVM能力，以便用户空间查询是否支持可缓存的PFNMAP。

这些补丁经过多位维护者的审核和测试，确保了在Grace Hopper/Blackwell平台上的兼容性，并为CUDA工作负载的运行提供了必要的支持。整体而言，这些改进将增强KVM在处理GPU设备内存时的灵活性和安全性。

#### 📝 邮件列表

1. **[07-05 07:17]** [PATCH v10 0/6] KVM: arm64: Map GPU device memory as cacheable
   - 发件人: ankita <ankita@nvidia.com>
2. **[07-05 07:17]** [PATCH v10 1/6] KVM: arm64: Rename the device variable to s2_force_noncacheable
   - 发件人: ankita <ankita@nvidia.com>
3. **[07-05 07:17]** [PATCH v10 2/6] KVM: arm64: Update the check to detect device memory
   - 发件人: ankita <ankita@nvidia.com>
4. **[07-05 07:17]** [PATCH v10 3/6] KVM: arm64: Block cacheable PFNMAP mapping
   - 发件人: ankita <ankita@nvidia.com>
5. **[07-05 07:17]** [PATCH v10 4/6] KVM: arm64: New function to determine hardware cache management support
   - 发件人: ankita <ankita@nvidia.com>
6. **[07-05 07:17]** [PATCH v10 5/6] KVM: arm64: Allow cacheable stage 2 mapping using VMA flags
   - 发件人: ankita <ankita@nvidia.com>
7. **[07-05 07:17]** [PATCH v10 6/6] KVM: arm64: Expose new KVM cap for cacheable PFNMAP
   - 发件人: ankita <ankita@nvidia.com>

---

### Thread 6: [PATCH 0/2] KVM: arm64: Fixes and clarifications for FEAT_S1POE

**📧 邮件数**: 7 | **👥 参与者**: 3 | **📅 开始时间**: Tue,  1 Jul 2025 16:16:46 +0100

#### 🤖 AI 总结

本邮件线程讨论了针对 KVM（Kernel-based Virtual Machine）在 arm64 架构上 FEAT_S1POE（S1 Privileged Overlay Enable）功能的修复和澄清。Marc Zyngier 提出了两个补丁，解决了当前 NV（Nested Virtualization）支持 S1POE 的一些问题。

第一个补丁（PATCH 1/2）主要是消除 wi->{e0,}poe 和 wr->{p,u}ov 之间的混淆，明确了它们的作用：wi->{e0,}poe 是对访问控制的输入，而 wr->{p,u}ov 是访问控制的结果。补丁重构了计算 S1 Overlay 权限的函数，以减少不必要的寄存器读取。

第二个补丁（PATCH 2/2）则关注于 WXN（Write eXecute Never）规则的实现，指出在 S1 Overlay 启用和禁用时，WXN 应分别适用于 Overlay 和基础权限。补丁将这两个规则分开处理，使代码更易于理解和验证。

本周的讨论中，Ben Horgan 提出了两个补丁，修复了 MDCR_EL2.HPMN 的上限强制执行问题，并确保在使用位域替换函数时检查返回值，以避免潜在错误。Zenghui Yu 对 Ben Horgan 的补丁进行了审核并表示认可。

总体来看，本周的讨论集中在对 KVM arm64 的权限管理和错误修复上，推动了相关功能的完善。

#### 📝 邮件列表

1. **[07-01 16:16]** [PATCH 0/2] KVM: arm64: Fixes and clarifications for FEAT_S1POE
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[07-01 16:16]** [PATCH 1/2] KVM: arm64: Remove the wi->{e0,}poe vs wr->{p,u}ov confusion
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[07-01 16:16]** [PATCH 2/2] KVM: arm64: Follow specification when implementing WXN
   - 发件人: Marc Zyngier <maz@kernel.org>
4. **[07-03 14:57]** [PATCH 0/2] Fix and add warning of misuse of type##_replace_bits()
   - 发件人: Ben Horgan <ben.horgan@arm.com>
5. **[07-03 14:57]** [PATCH 1/2] KVM: arm64: Fix enforcement of upper bound on MDCR_EL2.HPMN
   - 发件人: Ben Horgan <ben.horgan@arm.com>
6. **[07-03 14:57]** [PATCH 2/2] bitfield: Ensure the return value of type##_replace_bits() is checked
   - 发件人: Ben Horgan <ben.horgan@arm.com>
7. **[07-04 14:44]** Re: [PATCH 1/2] KVM: arm64: Fix enforcement of upper bound on
 MDCR_EL2.HPMN
   - 发件人: Zenghui Yu <yuzenghui@huawei.com>

---

### Thread 7: [PATCH v7 0/5] KVM: arm64: Support FF-A 1.2 and SEND_DIRECT2 ABI

**📧 邮件数**: 7 | **👥 参与者**: 2 | **📅 开始时间**: Tue, 01 Jul 2025 22:06:33 +0000

#### 🤖 AI 总结

本邮件线程讨论了一个关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下支持 FF-A 1.2 及其 SEND_DIRECT2 ABI 的补丁集（PATCH v7 0/5）。该补丁集的主要目的是引入 FF-A 1.2 规范中的新功能，特别是 SEND_DIRECT2 ABI，允许使用 x4-x17 寄存器作为消息负载。

在历史讨论中，补丁集的背景是为了确保主机不会使用低于已与虚拟机监控器协商的 FF-A 版本，因为监控器没有必要的兼容性路径来进行版本转换。补丁还更新了所有 SMC（Secure Monitor Call）调用，以使用 SMCCC 1.2（ARM Secure Monitor Call Convention），简化了需要接受超过 8 个参数和/或返回超过 4 个值的接口的支持。

本周的新讨论中，Per Larsen 提出了五个补丁，分别涉及到：1）修正主机版本降级尝试的返回值；2）在 FF-A 初始化和主机处理程序中使用 SMCCC 1.2；3）将 FFA_NOTIFICATION_* 接口标记为不支持；4）将支持的 FF-A 版本提升至 1.2；5）在主机处理程序中支持 FFA_MSG_SEND_DIRECT_REQ2。Marc Zyngier 对第二个补丁提出了质疑，认为在某些情况下，寄存器的保留问题可能导致不兼容，要求提供更有说服力的例子。

整体来看，本周的讨论集中在补丁的具体实现和潜在的兼容性问题上，显示出对 FF-A 1.2 支持的复杂性和重要性。

#### 📝 邮件列表

1. **[07-01 22:06]** [PATCH v7 0/5] KVM: arm64: Support FF-A 1.2 and SEND_DIRECT2 ABI
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>
2. **[07-01 22:06]** [PATCH v7 1/5] KVM: arm64: Correct return value on host version
 downgrade attempt
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>
3. **[07-01 22:06]** [PATCH v7 2/5] KVM: arm64: Use SMCCC 1.2 for FF-A initialization
 and in host handler
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>
4. **[07-01 22:06]** [PATCH v7 3/5] KVM: arm64: Mark FFA_NOTIFICATION_* calls as
 unsupported
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>
5. **[07-01 22:06]** [PATCH v7 4/5] KVM: arm64: Bump the supported version of FF-A to
 1.2
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>
6. **[07-01 22:06]** [PATCH v7 5/5] KVM: arm64: Support FFA_MSG_SEND_DIRECT_REQ2 in
 host handler
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>
7. **[07-03 13:38]** Re: [PATCH v7 2/5] KVM: arm64: Use SMCCC 1.2 for FF-A initialization and in host handler
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 8: [PATCH v2 2/5] irqchip/gic-v5: Populate struct gic_kvm_info

**📧 邮件数**: 7 | **👥 参与者**: 3 | **📅 开始时间**: Fri, 27 Jun 2025 10:09:01 +0000

#### 🤖 AI 总结

本邮件线程讨论了一个关于 GICv5 主机支持 GICv3 客户机的补丁，具体为「[PATCH v2 2/5] irqchip/gic-v5: Populate struct gic_kvm_info」。该补丁旨在根据 FEAT_GCIE_LEGACY 特性填充 gic_kvm_info 结构，以便 KVM 能够探测兼容的 GIC。

在历史讨论中，Sascha Bischoff 提出了这一系列补丁的背景，主要目的是使现有的 GICv3 虚拟机能够在 GICv5 系统上无缝运行，而无需对虚拟机或虚拟机监控程序进行修改。补丁的重点包括 KVM GIC 支持和 IRQ 芯片支持。

在本周的新讨论中，Lorenzo Pieralisi 对补丁进行了审核并表示通过。Jonathan Cameron 提出了关于代码格式的小建议，指出了标签块中的空行问题，并感谢 Sascha 的修正。Sascha 随后确认已解决这些问题，并感谢参与者的反馈。

总体来看，本周的讨论主要集中在补丁的审核和小的格式修正上，进展顺利。

#### 📝 邮件列表

1. **[06-27 10:09]** [PATCH v2 2/5] irqchip/gic-v5: Populate struct gic_kvm_info
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
2. **[06-27 10:09]** [PATCH v2 0/5] KVM: arm64: Enable GICv3 guests on GICv5 hosts using
 FEAT_GCIE_LEGACY
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
3. **[06-27 10:09]** [PATCH v2 1/5] irqchip/gic-v5: Skip deactivate for forwarded PPI
 interrupts
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
4. **[07-01 11:45]** Re: [PATCH v2 2/5] irqchip/gic-v5: Populate struct gic_kvm_info
   - 发件人: Lorenzo Pieralisi <lpieralisi@kernel.org>
5. **[07-02 15:28]** Re: [PATCH v2 1/5] irqchip/gic-v5: Skip deactivate for forwarded
 PPI interrupts
   - 发件人: Jonathan Cameron <Jonathan.Cameron@huawei.com>
6. **[07-03 08:58]** Re: [PATCH v2 1/5] irqchip/gic-v5: Skip deactivate for forwarded PPI
 interrupts
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
7. **[07-03 08:58]** Re: [PATCH v2 2/5] irqchip/gic-v5: Populate struct gic_kvm_info
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>

---

### Thread 9: [PATCH] ARM64: errata: Add workaround for HIP10/HIP10C erratum 162200803

**📧 邮件数**: 6 | **👥 参与者**: 2 | **📅 开始时间**: Thu, 26 Jun 2025 20:41:42 +0800

#### 🤖 AI 总结

本邮件讨论的主题是针对 ARM64 架构的 HIP10/HIP10C 错误（erratum 162200803）提出的补丁。该补丁旨在解决 GICv4.0 中 vPE 调度的一个硬件缺陷，即在多个 vPE 同时发送调度命令时，可能导致命令超时。

在历史讨论中，Zhou Wang 提出了补丁的初步方案，指出当前的实现无法有效限制 vLPI 的数量，Marc Zyngier 则质疑了补丁的有效性，并指出需要在 KVM 中增加对 vLPI 数量的检查，以避免超出限制的情况。此外，Zhou Wang 也承认需要在相关逻辑中引入 GICD.num_LPI 的使用。

在本周的新讨论中，Marc Zyngier 强调在实施补丁之前，必须确保能够正确保存和恢复限制，以支持迁移功能。Zhou Wang 提出了在 KVM 中将 GICD_TYPER.num_LPIs 作为默认配置的建议，以确保在迁移时逻辑的一致性。最后，Marc Zyngier 指出，GICD_TYPER 的默认配置应该是 0，以避免对现有系统的迁移造成影响。

总体来看，讨论集中在如何有效实施补丁以解决硬件缺陷，同时确保 KVM 的迁移功能不受影响。

#### 📝 邮件列表

1. **[06-26 20:41]** [PATCH] ARM64: errata: Add workaround for HIP10/HIP10C erratum 162200803
   - 发件人: Zhou Wang <wangzhou1@hisilicon.com>
2. **[06-26 14:27]** Re: [PATCH] ARM64: errata: Add workaround for HIP10/HIP10C erratum 162200803
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[06-27 14:36]** Re: [PATCH] ARM64: errata: Add workaround for HIP10/HIP10C erratum
 162200803
   - 发件人: Zhou Wang <wangzhou1@hisilicon.com>
4. **[07-01 09:14]** Re: [PATCH] ARM64: errata: Add workaround for HIP10/HIP10C erratum 162200803
   - 发件人: Marc Zyngier <maz@kernel.org>
5. **[07-02 17:57]** Re: [PATCH] ARM64: errata: Add workaround for HIP10/HIP10C erratum
 162200803
   - 发件人: Zhou Wang <wangzhou1@hisilicon.com>
6. **[07-03 11:44]** Re: [PATCH] ARM64: errata: Add workaround for HIP10/HIP10C erratum 162200803
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 10: [PATCH v3 00/10] perf: arm_spe: Armv8.8 SPE features

**📧 邮件数**: 6 | **👥 参与者**: 4 | **📅 开始时间**: Mon, 30 Jun 2025 14:26:14 +0100

#### 🤖 AI 总结

本邮件线程讨论了针对 ARMv8.8 SPE 特性的补丁系列（PATCH v3 00/10），主要集中在性能监控（perf）和 KVM 的相关更新。

1. **原始补丁内容**：该补丁系列旨在增强 ARMv8.8 架构下的 SPE（可编程事件监控）功能，包含多个补丁，涉及新的性能事件属性和文档更新。

2. **之前讨论要点**：虽然没有提供具体的历史讨论内容，但可以推测，补丁的提出是为了改进现有的性能监控机制，以适应新的硬件特性。

3. **本周新讨论与进展**：
   - James Clark 对补丁进行了提醒，显示出对该系列补丁的持续关注。
   - Ian Rogers 对多个补丁（如 perf_event_attr::config4 和工具头文件同步）给予了审核通过的反馈，表明这些补丁得到了认可。
   - Jinqian Yang 提出了在测试过程中发现的一个问题，涉及 KVM 中 ID 寄存器的写回逻辑，指出在特定配置下，寄存器的可见性变化需要更新 cpreg 列表，并提出了可能的解决方案。
   - Cornelia Huck 对 Jinqian Yang 的反馈表示感谢，并指出需要进一步思考寄存器可见性变化的影响。

总体来看，本周的讨论主要集中在补丁的审核和 KVM 中寄存器处理的问题上，显示出社区对 ARMv8.8 SPE 特性补丁的积极响应和深入探讨。

#### 📝 邮件列表

1. **[06-30 14:26]** Re: [PATCH v3 00/10] perf: arm_spe: Armv8.8 SPE features
   - 发件人: James Clark <james.clark@linaro.org>
2. **[06-30 08:35]** Re: [PATCH v3 06/10] perf: Add perf_event_attr::config4
   - 发件人: Ian Rogers <irogers@google.com>
3. **[06-30 08:36]** Re: [PATCH v3 08/10] tools headers UAPI: Sync linux/perf_event.h with
 the kernel sources
   - 发件人: Ian Rogers <irogers@google.com>
4. **[06-30 08:38]** Re: [PATCH v3 10/10] perf docs: arm-spe: Document new SPE filtering features
   - 发件人: Ian Rogers <irogers@google.com>
5. **[07-02 12:01]** Re: [PATCH v3 07/10] arm/kvm: write back modified ID regs to KVM
   - 发件人: Jinqian Yang <yangjinqian1@huawei.com>
6. **[07-02 10:46]** Re: [PATCH v3 07/10] arm/kvm: write back modified ID regs to KVM
   - 发件人: Cornelia Huck <cohuck@redhat.com>

---

### Thread 11: [PATCH v3 0/7] Add support for FEAT_{LS64, LS64_V} and related tests

**📧 邮件数**: 6 | **👥 参与者**: 2 | **📅 开始时间**: Thu, 26 Jun 2025 16:08:59 +0800

#### 🤖 AI 总结

本邮件线程讨论了对 Armv8.7 架构中新增的 FEAT_{LS64, LS64_V} 特性的支持，主要涉及如何在 KVM 中处理与这些特性相关的内存访问异常。

1. **原始 patch/问题的内容**：Yicong Yang 提出的补丁（PATCH v3 0/7）旨在为 Armv8.7 的 FEAT_{LS64, LS64_V} 特性提供支持，包括在 CPU 特性列表中添加识别和启用这些特性、通过 HWCAP3 和 cpuinfo 向用户空间暴露支持信息、添加相关的硬件能力测试，以及在虚拟机中处理不支持的内存访问的异常。

2. **之前的讨论要点**：在历史讨论中，Marc Zyngier 对补丁中处理 DABT（数据异常）的问题提出了质疑，认为在某些情况下，虚拟机监控器（VMM）不应介入处理异常，而应直接将异常反馈给用户空间。讨论中还涉及了对权限故障和不支持的原子访问的处理方式。

3. **本周的新讨论、进展或结论**：在本周的讨论中，Yicong Yang 和 Marc Zyngier 达成了一致，支持在 LS64WB 缺失的平台上注入不支持的原子访问异常（UAoEF），以确保处理的一致性。这一决定旨在允许在正常情况下使用这些指令，尽管平台不支持 LS64WB，从而避免对设备内存的使用造成不公平限制。

#### 📝 邮件列表

1. **[06-26 16:08]** [PATCH v3 0/7] Add support for FEAT_{LS64, LS64_V} and related tests
   - 发件人: Yicong Yang <yangyicong@huawei.com>
2. **[06-26 16:09]** [PATCH v3 3/7] KVM: arm64: Handle DABT caused by LS64* instructions on unsupported memory
   - 发件人: Yicong Yang <yangyicong@huawei.com>
3. **[06-26 09:51]** Re: [PATCH v3 3/7] KVM: arm64: Handle DABT caused by LS64* instructions on unsupported memory
   - 发件人: Marc Zyngier <maz@kernel.org>
4. **[06-26 19:39]** Re: [PATCH v3 3/7] KVM: arm64: Handle DABT caused by LS64*
 instructions on unsupported memory
   - 发件人: Yicong Yang <yangyicong@huawei.com>
5. **[06-27 14:12]** Re: [PATCH v3 3/7] KVM: arm64: Handle DABT caused by LS64* instructions on unsupported memory
   - 发件人: Marc Zyngier <maz@kernel.org>
6. **[07-01 20:31]** Re: [PATCH v3 3/7] KVM: arm64: Handle DABT caused by LS64*
 instructions on unsupported memory
   - 发件人: Yicong Yang <yangyicong@huawei.com>

---

### Thread 12: [PATCH 0/3] arm64: Support FEAT_LSFE (Large System Float
 Extension)

**📧 邮件数**: 6 | **👥 参与者**: 2 | **📅 开始时间**: Fri, 27 Jun 2025 18:20:43 +0100

#### 🤖 AI 总结

本邮件线程讨论了对 ARM64 架构的 FEAT_LSFE（大型系统浮点扩展）的支持，包含三个补丁。FEAT_LSFE 是从 v9.5 版本开始可选的，旨在为浮点值的原子内存操作提供新指令。尽管内核当前没有直接使用该特性，但补丁提供了一个硬件能力（hwcap），以便用户空间能够发现该特性，并允许 KVM 客户端访问相关 ID 寄存器。

在历史讨论中，Mark Brown 提出了三个补丁，分别是：1）为 FEAT_LSFE 添加 hwcap；2）在 KVM 中向客户机暴露 FEAT_LSFE；3）在自测试中将 lsfe 添加到 hwcaps 测试中。讨论中指出，FEAT_LSFE 不会引入新的架构状态，因此仅需提供 hwcap 以支持用户空间的发现。

在本周的新讨论中，Ben Horgan 对补丁进行了审查，提出了一些小的修改建议，并表示整体看起来不错。他提到自己是新加入的成员，认为需要更有经验的审查者来进行深入评估。最终，Ben 对补丁给予了认可（Reviewed-by）。

#### 📝 邮件列表

1. **[06-27 18:20]** [PATCH 0/3] arm64: Support FEAT_LSFE (Large System Float
 Extension)
   - 发件人: Mark Brown <broonie@kernel.org>
2. **[06-27 18:20]** [PATCH 1/3] arm64/hwcap: Add hwcap for FEAT_LSFE
   - 发件人: Mark Brown <broonie@kernel.org>
3. **[06-27 18:20]** [PATCH 3/3] kselftest/arm64: Add lsfe to the hwcaps test
   - 发件人: Mark Brown <broonie@kernel.org>
4. **[06-30 11:05]** Re: [PATCH 1/3] arm64/hwcap: Add hwcap for FEAT_LSFE
   - 发件人: Ben Horgan <ben.horgan@arm.com>
5. **[06-30 11:08]** Re: [PATCH 3/3] kselftest/arm64: Add lsfe to the hwcaps test
   - 发件人: Ben Horgan <ben.horgan@arm.com>
6. **[06-30 11:21]** Re: [PATCH 0/3] arm64: Support FEAT_LSFE (Large System Float
 Extension)
   - 发件人: Ben Horgan <ben.horgan@arm.com>

---

### Thread 13: [PATCH v6 00/28] KVM: arm64: Implement support for SME

**📧 邮件数**: 4 | **👥 参与者**: 2 | **📅 开始时间**: Wed, 25 Jun 2025 11:47:51 +0100

#### 🤖 AI 总结

本邮件线程讨论了针对 KVM（内核虚拟机）在 arm64 架构下实现对 SME（Scalable Matrix Extension）支持的补丁系列，特别是第 18 个补丁，涉及 SME 优先级寄存器的支持。

**原始补丁内容**：补丁系列的目标是实现对 SME 的支持，主要关注用户空间 ABI 的设计，包括 SVE 寄存器的向量长度、寄存器访问及其与 PSTATE.{SM,ZA} 状态的关系。此外，还讨论了如何在 KVM 中实现细粒度陷阱控制。

**之前讨论要点**：在历史讨论中，Mark Brown 提出了对寄存器设计的反馈，特别是关于寄存器返回值总是为零的合理性，以及是否可以在需要时动态生成该值。Marc Zyngier 也对寄存器的处理提出了疑问，强调了在虚拟机访问时可能出现的错误。

**本周新讨论进展**：在本周的讨论中，Mark Brown 表示将根据之前的反馈调整处理方式，决定不再在 sysreg 文件中设置该寄存器，而是选择动态合成。双方确认了在 NV 超级管理程序下，寄存器访问将被正常处理，避免了不必要的复杂性。

总体来看，讨论围绕着如何更有效地实现 SME 寄存器的支持展开，参与者在设计细节上进行了深入的交流和调整。

#### 📝 邮件列表

1. **[06-25 11:47]** [PATCH v6 00/28] KVM: arm64: Implement support for SME
   - 发件人: Mark Brown <broonie@kernel.org>
2. **[06-25 11:48]** [PATCH v6 18/28] KVM: arm64: Support SME priority registers
   - 发件人: Mark Brown <broonie@kernel.org>
3. **[06-29 10:32]** Re: [PATCH v6 18/28] KVM: arm64: Support SME priority registers
   - 发件人: Marc Zyngier <maz@kernel.org>
4. **[07-03 19:03]** Re: [PATCH v6 18/28] KVM: arm64: Support SME priority registers
   - 发件人: Mark Brown <broonie@kernel.org>

---

### Thread 14: [PATCH v2 0/3] arm64: Support FEAT_LSFE (Large System Float
 Extension)

**📧 邮件数**: 4 | **👥 参与者**: 1 | **📅 开始时间**: Thu, 03 Jul 2025 17:23:21 +0100

#### 🤖 AI 总结

本邮件线程讨论的主题是关于对 ARM64 架构的 FEAT_LSFE（大系统浮点扩展）的支持。该扩展在 v9.5 版本中为可选特性，主要提供原子浮点内存操作的新指令。由于内核当前没有对该特性的直接需求，因此提议在用户空间中提供一个硬件能力标志（hwcap），以便用户能够发现这一特性，并允许 KVM 客户机访问相关的 ID 寄存器字段。

在本周的讨论中，Mark Brown 提出了三个补丁：第一个补丁为 FEAT_LSFE 添加 hwcap，以支持用户空间的发现；第二个补丁则是将 FEAT_LSFE 的相关 ID 寄存器字段暴露给 KVM 客户机；第三个补丁则是将 LSFE 添加到 kselftest 的 hwcaps 测试中。所有补丁都经过了相应的代码修改，并附上了详细的变更记录。

本周的进展主要集中在补丁的具体实现上，包括对 hwcap 的定义、KVM 的寄存器暴露以及自测试的更新，确保了新特性的正确性和可用性。

#### 📝 邮件列表

1. **[07-03 17:23]** [PATCH v2 0/3] arm64: Support FEAT_LSFE (Large System Float
 Extension)
   - 发件人: Mark Brown <broonie@kernel.org>
2. **[07-03 17:23]** [PATCH v2 1/3] arm64/hwcap: Add hwcap for FEAT_LSFE
   - 发件人: Mark Brown <broonie@kernel.org>
3. **[07-03 17:23]** [PATCH v2 2/3] KVM: arm64: Expose FEAT_LSFE to guests
   - 发件人: Mark Brown <broonie@kernel.org>
4. **[07-03 17:23]** [PATCH v2 3/3] kselftest/arm64: Add lsfe to the hwcaps test
   - 发件人: Mark Brown <broonie@kernel.org>

---

### Thread 15: [PATCH] KVM: arm64: Fix handling of FEAT_GTG for unimplemented granule sizes

**📧 邮件数**: 4 | **👥 参与者**: 2 | **📅 开始时间**: Tue,  1 Jul 2025 15:22:25 +0100

#### 🤖 AI 总结

本邮件线程讨论了一个针对 KVM（Kernel-based Virtual Machine）在 arm64 架构下的补丁，旨在修复对未实现的 granule 大小的 FEAT_GTG 处理问题。补丁的主要内容是添加新的检查，以确保在向虚拟机发布 granule 大小时，只有实际支持的大小才会被广告，从而避免在只支持 4kB 和 64kB 页大小的系统中错误地宣传 16kB 支持的问题。

在之前的讨论中，Marc Zyngier 提到，当前的处理方式可能导致在启动 EL2 虚拟机时出现不一致的情况，尤其是在硬件只支持部分页大小的情况下。Oliver Upton 也对此表示认同，并指出虽然这种情况在技术上是可行的，但在 S1 和 S2 的 granularity 不匹配时可能会引发更复杂的问题。

本周的新进展包括 Oliver 对补丁的审查和认可，并建议在补丁的变更日志中进一步阐明其合理性。Marc 随后更新了日志，并确认补丁已被应用到修复集中。整体来看，讨论围绕着确保 KVM 的稳定性和一致性展开，补丁得到了积极的反馈和最终的采纳。

#### 📝 邮件列表

1. **[07-01 15:22]** [PATCH] KVM: arm64: Fix handling of FEAT_GTG for unimplemented granule sizes
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[07-01 19:35]** Re: [PATCH] KVM: arm64: Fix handling of FEAT_GTG for unimplemented
 granule sizes
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
3. **[07-03 09:52]** Re: [PATCH] KVM: arm64: Fix handling of FEAT_GTG for unimplemented granule sizes
   - 发件人: Marc Zyngier <maz@kernel.org>
4. **[07-03 10:41]** Re: [PATCH] KVM: arm64: Fix handling of FEAT_GTG for unimplemented granule sizes
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 16: [PATCH v6 0/5] KVM: arm64: Support FF-A 1.2 and SEND_DIRECT2 ABI

**📧 邮件数**: 3 | **👥 参与者**: 2 | **📅 开始时间**: Fri, 27 Jun 2025 07:12:24 +0000

#### 🤖 AI 总结

本邮件线程讨论了关于 KVM（Kernel-based Virtual Machine）在 arm64 架构上对 FF-A 1.2 及 SEND_DIRECT2 ABI 的支持，主要由 Per Larsen 提出了一系列补丁（patch）。

1. **原始 patch/问题的内容**：
   原始补丁集的目的是为了支持 FF-A 1.2 规范，该规范引入了新的 SEND_DIRECT2 ABI，允许使用寄存器 x4-x17 作为消息负载。补丁确保主机不会使用低于已与虚拟机监控器（hypervisor）协商的 FF-A 版本，以避免兼容性问题。

2. **之前的讨论要点**：
   在之前的讨论中，Per Larsen 提到需要更新 FF-A 版本以支持新的消息接口，并引入了使用 SMCCC 1.2 的必要性，以确保与 FF-A 1.2 的兼容性。此外，补丁还涉及到对 FF-A 版本的标记和相关函数的更新。

3. **本周的新讨论、进展或结论**：
   本周，Marc Zyngier 对补丁提出了一些建议，询问某些字段是否为可选，并建议检查 MBZ 字段是否仍为 0，强调使用 GENMASK 来更清晰地表达掩码的意图。这些反馈为补丁的进一步完善提供了方向。

总体而言，这一讨论围绕着增强 KVM 对 FF-A 1.2 的支持，确保系统的兼容性和功能性。

#### 📝 邮件列表

1. **[06-27 07:12]** [PATCH v6 0/5] KVM: arm64: Support FF-A 1.2 and SEND_DIRECT2 ABI
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>
2. **[06-27 07:12]** [PATCH v6 4/5] KVM: arm64: Bump the supported version of FF-A to
 1.2
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>
3. **[06-30 09:41]** Re: [PATCH v6 4/5] KVM: arm64: Bump the supported version of FF-A to 1.2
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 17: [PATCH v23 4/4] perf: arm_pmuv3: Add support for the Branch
 Record Buffer Extension (BRBE)

**📧 邮件数**: 2 | **👥 参与者**: 1 | **📅 开始时间**: Fri, 4 Jul 2025 18:18:24 +0100

#### 🤖 AI 总结

本邮件线程讨论的主题是关于为 ARM 架构的性能监控单元（PMU）添加对分支记录缓冲区扩展（BRBE）的支持的补丁（PATCH v23 4/4）。该补丁旨在改进分支记录的处理，以避免在事件溢出时出现记录不连续的问题。

在历史讨论中，补丁的初步版本已被提出，主要关注如何在事件溢出时有效管理分支记录。补丁的变更日志提到，重构了 BRBE 的无效化逻辑，以避免在中断处理程序中无效化记录，从而确保多用户场景下的记录完整性。

在本周的新讨论中，参与者 Mark Rutland 对补丁的当前状态表示满意，并提出了一些修正建议，包括将无效化操作移至 `brbe_enable()` 函数中，以避免在处理多个事件溢出时仅第一个事件接收记录的问题。此外，他还建议将 `armv8pmu_restart()` 函数合并回 `armv8pmu_start()` 函数中。Mark 还确认了对整个补丁系列的认可，表示将很快进行应用。

总的来说，本周的讨论集中在对补丁细节的优化和确认上，推动了补丁的最终应用进程。

#### 📝 邮件列表

1. **[07-04 18:18]** Re: [PATCH v23 4/4] perf: arm_pmuv3: Add support for the Branch
 Record Buffer Extension (BRBE)
   - 发件人: Mark Rutland <mark.rutland@arm.com>
2. **[07-04 18:20]** Re: [PATCH v23 0/4] arm64/perf: Enable branch stack sampling
   - 发件人: Mark Rutland <mark.rutland@arm.com>

---

### Thread 18: [PATCH] KVM: arm64: Remove kvm_arch_vcpu_run_map_fp()

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Thu, 19 Jun 2025 14:48:17 +0100

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的一个补丁，旨在移除函数 `kvm_arch_vcpu_run_map_fp()`。在历史讨论中，Mark Rutland 提到，之前 KVM 的 hyp 代码需要将主机的 FPSIMD 状态保存到主机的 `fpsimd_state` 内存中，并在运行 vCPU 之前将其映射到 hyp 的 Stage-1 映射中。然而，随着两个提交（fbc7e61195e2 和 8eca7f6d5100）的引入，这一过程已不再必要，因为现在在调用 hyp 运行 vCPU 之前，主机的 FPSIMD 状态会被主动保存。

在本周的新讨论中，Marc Zyngier 确认了该补丁的应用，并表示感谢。这表明补丁已被接受并合并到修复版本中，标志着这一问题的解决。

总结而言，此次讨论围绕移除不再需要的函数展开，历史背景提供了必要的技术细节，而本周的进展则确认了补丁的成功应用。

#### 📝 邮件列表

1. **[06-19 14:48]** [PATCH] KVM: arm64: Remove kvm_arch_vcpu_run_map_fp()
   - 发件人: Mark Rutland <mark.rutland@arm.com>
2. **[07-03 10:40]** Re: [PATCH] KVM: arm64: Remove kvm_arch_vcpu_run_map_fp()
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 19: [PATCH] KVM: arm64: preserve pending during kvm_irqfd_deassign

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Wed,  2 Jul 2025 07:41:37 -0700

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 ARM64 架构下处理中断的一个补丁，具体是关于在 `kvm_irqfd_deassign` 函数中保留待处理的中断状态。

**原始补丁内容**：
补丁的主要目的是在调用 `kvm_vgic_v4_unset_forwarding` 时，如果有中断处于待处理状态，则将其转移到生产者的 eventfd 中。这样，如果 KVM 实例随后被销毁，中断状态将被保留，以便在新 KVM 实例中重新创建时能够恢复。

**之前讨论要点**：
在之前的讨论中，Steve Sistare 提出这个补丁是为了支持 QEMU 的实时更新功能，允许在不暂停 VFIO 中断的情况下重新创建 KVM 实例。然而，Oliver Upton 对此表示质疑，指出这种处理方式可能会导致中断丢失或产生系统错误，并提到 KVM 已经提供了保存待处理状态的 ioctl 接口，用户空间应负责中断生成器的暂停。

**本周新讨论、进展或结论**：
本周的讨论中，Oliver Upton 强调了补丁的潜在问题，认为 KVM 不应主动转发待处理状态，尤其是在硬件不支持的情况下。他指出，现有的状态保存/恢复机制已经足够，用户空间如果需要特殊处理，应自行解决。整体来看，Oliver 对补丁的必要性表示怀疑，并认为当前的实现可能会引入更多问题。

#### 📝 邮件列表

1. **[07-02 07:41]** [PATCH] KVM: arm64: preserve pending during kvm_irqfd_deassign
   - 发件人: Steve Sistare <steven.sistare@oracle.com>
2. **[07-02 08:19]** Re: [PATCH] KVM: arm64: preserve pending during kvm_irqfd_deassign
   - 发件人: Oliver Upton <oliver.upton@linux.dev>

---

### Thread 20: [PATCH v3 09/22] KVM: arm64: Correct kvm_arm_pmu_get_max_counters()

**📧 邮件数**: 2 | **👥 参与者**: 1 | **📅 开始时间**: Mon, 30 Jun 2025 17:42:42 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的性能监控单元（PMU）计数器的修正，具体涉及到函数 `kvm_arm_pmu_get_max_counters()` 的补丁（PATCH v3 09/22）。

在历史讨论中，虽然没有具体的邮件记录，但可以推测该补丁旨在解决 PMU 计数器的最大值计算问题，确保在不同的分区状态下能够正确返回计数器的数量。

本周的新讨论中，Colton Lewis 和 Marc Zyngier 进行了深入交流。Marc 提到在没有分区的情况下，`hpmn_max` 的值应为 0，这个值虽然有效，但在分区情况下需要返回正确的计数器数量。Colton 进一步解释了他的逻辑，即 `hpmn_max` 只有在 PMU 被分区时才是有效的，若将其设为 0，则需要引入额外的标志来判断分区状态。

总体来看，本周的讨论集中在如何处理 PMU 的分区逻辑以及相应的计数器返回值上，尚未达成最终结论，但对补丁的理解和实现细节进行了重要的澄清。

#### 📝 邮件列表

1. **[06-30 17:42]** Re: [PATCH v3 09/22] KVM: arm64: Correct kvm_arm_pmu_get_max_counters()
   - 发件人: Colton Lewis <coltonlewis@google.com>
2. **[06-30 17:42]** Re: [PATCH v3 02/22] arm64: Generate sign macro for sysreg Enums
   - 发件人: Colton Lewis <coltonlewis@google.com>

---

### Thread 21: [PATCH V5 0/2] arm64/debug: Drop redundant DBG_MDSCR_* macros

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Thu,  3 Jul 2025 20:02:11 +0100

#### 🤖 AI 总结

本邮件讨论的主题是关于一个针对 ARM64 架构的补丁，主要目的是删除冗余的 DBG_MDSCR_* 宏。补丁的具体内容包括两个部分：第一部分是删除冗余的宏定义，第二部分是对 KVM 自测中 MDSCR_EL1 寄存器相关变量的数据类型进行修改。

在历史讨论中，虽然没有具体的邮件记录，但可以推测该补丁的提出是为了简化代码和提高可读性，避免不必要的宏定义对代码维护的影响。

在本周的新讨论中，参与者 Catalin Marinas 确认已将该补丁应用到 arm64 的开发分支（for-next/mdscr-cleanup），并对补丁的提交表示感谢。这表明该补丁得到了认可并已进入后续开发流程，显示出对代码清理工作的积极响应。

#### 📝 邮件列表

1. **[07-03 20:02]** Re: [PATCH V5 0/2] arm64/debug: Drop redundant DBG_MDSCR_* macros
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>

---

### Thread 22: [PATCH v2 1/6] KVM: arm64: VM exit to userspace to handle SEA

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Tue, 1 Jul 2025 10:35:32 -0700

#### 🤖 AI 总结

本邮件主题为“[PATCH v2 1/6] KVM: arm64: VM exit to userspace to handle SEA”，主要讨论了在 KVM（Kernel-based Virtual Machine）环境下，ARM64 架构如何处理虚拟机退出到用户空间以应对 SEA（System Error Acknowledgment）的问题。

在历史讨论中，并未提供具体的上下文或先前的讨论内容，因此我们无法详细了解该补丁的背景或之前的讨论要点。

本周的讨论中，参与者 Jiaqi Yan 提出了对该补丁的请求，希望能获得更多的审查和反馈。这表明该补丁可能尚未得到充分的评估，且作者希望推动其进展。

综上所述，该补丁旨在改善 KVM 在 ARM64 架构下的错误处理机制，目前仍在等待社区的反馈和审查。

#### 📝 邮件列表

1. **[07-01 10:35]** Re: [PATCH v2 1/6] KVM: arm64: VM exit to userspace to handle SEA
   - 发件人: Jiaqi Yan <jiaqiyan@google.com>

---

### Thread 23: [PATCH v7] coccinelle: misc: Add field_modify script

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Tue, 1 Jul 2025 20:38:24 +0800

#### 🤖 AI 总结

本邮件讨论的主题是一个名为「[PATCH v7] coccinelle: misc: Add field_modify script」的补丁，旨在通过引入一个新的宏 `FIELD_MODIFY()` 来优化内核中的字段修改模式。该宏的作用是替代原有的手动编码方式，提供编译时参数类型检查，以减少潜在的错误。

在历史讨论中，该补丁经过多次版本迭代，主要集中在如何改进 Coccinelle 脚本以自动化转换字段修改的代码。补丁的早期版本中，作者根据反馈逐步简化了条件选择，并去除了不必要的 ARM64 相关补丁。最终版本中，补丁成功地将四个原有的手动编码实例转换为使用新的 `FIELD_MODIFY()` 宏的形式。

在本周的新讨论中，作者 Luo Jie 提交了补丁的第七个版本，进一步优化了报告模式的字符串格式，并提供了对之前版本的链接以便于追踪变更。补丁的实现已在 IPQ9574 SoC 上进行验证，确保其在 ARM64 架构下的有效性。整体来看，本周的进展主要是对补丁的细节进行完善，并未出现新的争议或问题。

#### 📝 邮件列表

1. **[07-01 20:38]** [PATCH v7] coccinelle: misc: Add field_modify script
   - 发件人: Luo Jie <quic_luoj@quicinc.com>

---

## 📌 GIT PULL

共 1 个 thread

---

### Thread 1: [GIT PULL] KVM/arm64 fixes for 6.16, take #5

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Thu,  3 Jul 2025 11:05:44 +0100

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM/arm64 在 6.16 版本中的修复，Marc Zyngier 提出了本周的更新。

1. **原始 patch/问题的内容**：本周的补丁主要涉及对 KVM/arm64 的一些修复，包括删除过去修复中遗留的内容，具体是去除主机 FPSIMD 状态的 EL1 S1 映射，并停止向客户机报告错误的 S2 基础粒度大小。

2. **之前的讨论要点**：由于本周邮件中没有提及历史讨论，因此可以推测之前的讨论主要集中在对 KVM/arm64 的修复和优化上，且每周都有一个补丁请求的趋势，修复的严重性逐渐降低。

3. **本周的新讨论、进展或结论**：Marc Zyngier 本周的邮件强调了当前修复的内容，并期望将其与上周的 kvmarm-fixes-6.16-4 补丁请求一起处理。他提到的具体修改包括删除不必要的代码和修复对未实现粒度大小的处理。这些更改旨在提升 KVM/arm64 的稳定性和性能。

#### 📝 邮件列表

1. **[07-03 11:05]** [GIT PULL] KVM/arm64 fixes for 6.16, take #5
   - 发件人: Marc Zyngier <maz@kernel.org>

---

## 📌 Other

共 3 个 thread

---

### Thread 1: [kvm-unit-tests PATCH 0/2] scripts: extra_params rework

**📧 邮件数**: 7 | **👥 参与者**: 3 | **📅 开始时间**: Wed, 25 Jun 2025 16:43:52 +0100

#### 🤖 AI 总结

本邮件线程讨论了对 KVM 单元测试脚本的重构，主要集中在对 `extra_params` 参数的修改及其与 kvmtool 的兼容性。

**原始 patch/问题的内容**：
Alexandru Elisei 提出了一个补丁系列，目的是重构 KVM 单元测试脚本中的参数处理，以便支持 kvmtool。该系列补丁包括将 `extra_params` 重命名为 `qemu_params`，并添加一个新的测试定义参数 `test_args`，以便在 arm 和 arm64 架构下支持 kvmtool。

**之前讨论要点**：
在历史讨论中，Alexandru 解释了为何需要这些改动，强调了 kvmtool 和 qemu 在虚拟机运行语法上的不同。补丁旨在清晰地区分这两者的命令行选项，并为未来的 kvmtool 支持做好准备。

**本周的新讨论、进展或结论**：
在本周的讨论中，Andrew Jones 请求对补丁进行确认以便合并。Thomas Huth 对两个补丁提供了认可（Ack），并指出需要调整某些格式问题。最终，Andrew Jones 宣布补丁已被合并，标志着这一系列改动的成功实施。

#### 📝 邮件列表

1. **[06-25 16:43]** [kvm-unit-tests PATCH 0/2] scripts: extra_params rework
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
2. **[06-25 16:43]** [kvm-unit-tests PATCH 1/2] scripts: unittests.cfg: Rename 'extra_params' to 'qemu_params'
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
3. **[06-25 16:43]** [kvm-unit-tests PATCH 2/2] scripts: Add 'test_args' test definition parameter
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
4. **[07-02 15:23]** Re: [kvm-unit-tests PATCH 0/2] scripts: extra_params rework
   - 发件人: Andrew Jones <andrew.jones@linux.dev>
5. **[07-02 16:07]** Re: [kvm-unit-tests PATCH 1/2] scripts: unittests.cfg: Rename
 'extra_params' to 'qemu_params'
   - 发件人: Thomas Huth <thuth@redhat.com>
6. **[07-02 16:09]** Re: [kvm-unit-tests PATCH 2/2] scripts: Add 'test_args' test
 definition parameter
   - 发件人: Thomas Huth <thuth@redhat.com>
7. **[07-04 10:41]** Re: [kvm-unit-tests PATCH 0/2] scripts: extra_params rework
   - 发件人: Andrew Jones <andrew.jones@linux.dev>

---

### Thread 2: [kvm-unit-tests PATCH 0/2] riscv: Add kvmtool support

**📧 邮件数**: 3 | **👥 参与者**: 1 | **📅 开始时间**: Fri,  4 Jul 2025 17:12:55 +0200

#### 🤖 AI 总结

本邮件讨论的主题是为 RISC-V 架构添加对 kvmtool 的支持，包含两个补丁。

第一个补丁主要针对 ARM 和 ARM64 架构，确保在非 ARM 主机上运行 kvmtool 时的架构检查。该补丁通过在 `arm/run` 脚本中添加条件判断，确保只有在主机为 ARM 或 AArch64 时，kvmtool 才能正常工作。

第二个补丁则是为 RISC-V 架构添加 kvmtool 支持，使其能够像 ARM 和 ARM64 一样，作为一等公民运行测试。补丁中对多个脚本进行了修改，确保 RISC-V 能够正确调用 kvmtool，并在 README 文档中更新了相关说明，指出 RISC-V 也支持使用 kvmtool 运行测试。

在本周的新讨论中，Andrew Jones 提交了这两个补丁，并详细说明了每个补丁的功能及其代码变更。整体来看，讨论集中在增强 RISC-V 支持 kvmtool 的能力，以及确保在不同架构下的兼容性和正确性。

#### 📝 邮件列表

1. **[07-04 17:12]** [kvm-unit-tests PATCH 0/2] riscv: Add kvmtool support
   - 发件人: Andrew Jones <andrew.jones@linux.dev>
2. **[07-04 17:12]** [kvm-unit-tests PATCH 1/2] arm/arm64: Ensure proper host arch with kvmtool
   - 发件人: Andrew Jones <andrew.jones@linux.dev>
3. **[07-04 17:12]** [kvm-unit-tests PATCH 2/2] riscv: Add kvmtool support
   - 发件人: Andrew Jones <andrew.jones@linux.dev>

---

### Thread 3: [kvm-unit-tests PATCH v4 00/13] arm/arm64: Add kvmtool to the runner script

**📧 邮件数**: 3 | **👥 参与者**: 2 | **📅 开始时间**: Wed, 25 Jun 2025 16:48:00 +0100

#### 🤖 AI 总结

本邮件线程讨论了一个关于在 KVM 单元测试中添加 kvmtool 到运行脚本的补丁（PATCH v4 00/13）。该补丁旨在简化用户的测试流程，用户可以通过配置命令自动运行所有测试，特别是因为 kvmtool 相较于 qemu 更小且易于修改，适合开发者在 KVM 中添加或原型化新特性。

在历史讨论中，Alexandru Elisei 提出了该补丁的背景，强调了使用 kvmtool 的优势，特别是在测试的可靠性和自动化方面。补丁的实施将使得 KVM 开发者能够更高效地进行测试。

在本周的新讨论中，Andrew Jones 向其他参与者询问是否可以对该补丁进行确认（ack），以便进行合并。随后，Andrew Jones 在另一封邮件中确认该补丁已被合并，表示感谢。这表明该补丁得到了认可并成功推进。

#### 📝 邮件列表

1. **[06-25 16:48]** [kvm-unit-tests PATCH v4 00/13] arm/arm64: Add kvmtool to the runner script
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
2. **[07-02 15:25]** Re: [kvm-unit-tests PATCH v4 00/13] arm/arm64: Add kvmtool to the
 runner script
   - 发件人: Andrew Jones <andrew.jones@linux.dev>
3. **[07-04 10:41]** Re: [kvm-unit-tests PATCH v4 00/13] arm/arm64: Add kvmtool to the
 runner script
   - 发件人: Andrew Jones <andrew.jones@linux.dev>

---

